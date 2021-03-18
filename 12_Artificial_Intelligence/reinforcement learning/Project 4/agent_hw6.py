from rl_glue import BaseAgent
import numpy as np
import random
from random import randint
import tile3 as tile


class Agent(BaseAgent):
    """

    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """

    def __init__(self):
        """Declare agent variables."""
        self.actions_list = []
        self.action = None
        self.state = None
        self.prevState = None
        self.policy = None

        self.weight = []
        self.Z = []
        self.F = []

        self.memorySize = None
        self.num_tilings = None
        self.shape = []
        self.alpha = None
        self.lam = None
        self.epsilon = None
        self.gamma = None
        self.iht = None
        self.x = []
    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        """
        self.actions_list = [0,1,2]
        self.memorySize = 2048
        self.num_tilings = 8
        self.iht= tile.IHT(self.memorySize)

        self.weight = np.zeros(self.memorySize)
        for i in range(self.memorySize):
            self.weight[i] = np.random.uniform(-0.001,0)


        self.shape = np.zeros(64)

        self.alpha = 0.1
        self.lam = 0.9
        self.epsilon = 0
        self.gamma = 1



    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        """
        self.Z = np.zeros(self.memorySize)

        F0 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[0])
        F1 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[1])
        F2 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[2])

        Q0 = 0
        Q1 = 0
        Q2 = 0
        for i in F0:
            Q0 += self.weight[i]
        for i in F1:
            Q1 += self.weight[i]
        for i in F2:
            Q2 += self.weight[i]
        #Q0  = self.weight[F0].sum()
        #Q1  = self.weight[F1].sum()
        #Q2  = self.weight[F2].sum()

        self.state = state

        A = np.argmax([Q0, Q1, Q2])
        temp = [F0,F1,F2]
        self.F = temp[A]
        return A

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        """

        delta = reward
        F = self.F

        for i in F:
            delta = delta - self.weight[i]
            self.Z[i] = 1

        F0 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[0])
        F1 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[1])
        F2 = tile.tiles(self.iht,8,[8*state[0]/(0.5+1.2),8*state[1]/(0.07+0.07)],[2])

        Q0 = 0
        Q1 = 0
        Q2 = 0
        for i in F0:
            Q0 += self.weight[i]
        for i in F1:
            Q1 += self.weight[i]
        for i in F2:
            Q2 += self.weight[i]


        #Q0  = self.weight[F0].sum()
        #Q1  = self.weight[F1].sum()
        #Q2  = self.weight[F2].sum()

        A = np.argmax([Q0, Q1, Q2])
        temp = [F0,F1,F2]
        for i in temp[A]:
            delta += self.gamma*self.weight[i]
        self.weight += self.alpha*delta*self.Z
        self.Z *= self.gamma*self.lam

        self.F = temp[A]

        return A


    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        """
        delta = reward
        self.weight += self.alpha*delta*self.Z




    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'Q3':
            values = np.zeros((50,50))
            steps = 50
            numActions = 3
            for i in range(steps):
                for j in range(steps):
                    Q = np.zeros(3)
                    for a in range(numActions):

                        inds = tile.tiles(self.iht,8,[(-1.2 + (i * 1.7 / steps)),(-0.07 + (j * 0.14 / steps))], [a])

                        total_weight = np.sum(self.weight[inds])
                        Q[a] = total_weight


                    a = np.max(Q)
                    values[i][j] = -a

            np.save('values', values)
        else:
            return "I dont know how to respond to this message!!"

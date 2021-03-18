from rl_glue import BaseAgent
import numpy as np
import random
from random import randint


class Agent(BaseAgent):
    """

    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """

    def __init__(self):
        """Declare agent variables."""

        self.gamma = None
        self.alpha = None
        self.weight =None
        self.v= None

        self.policy = []
        self.state = None
        self.prevState = None
        self.episode_counter = None

    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        """
        self.alpha = 0.5
        self.gamma = 1


        self.policy = []
        for i in range(1000):
            num = randint(1,2)
            if num == 1:
                self.policy.append(1)

            else:
                self.policy.append(-1)
        self.policy = np.asarray(self.policy)


        self.weight = np.zeros(1001)

        self.episode_counter = 0


    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        """
        self.state = state
        self.episode_counter = self.episode_counter + 1



    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: reward, state, action, is_terminal = rlg.rl_step()
            if is_terminal == True:action - integer
        """
        self.state = state
        self.episode_counter +=1
        x = np.zeros(1001)

        x[self.state] = 1
        first = self.gamma * self.weight.dot(x)
        #print('first: ', first)

        x[self.state] = 0
        x[self.prevState] = 1
        second =self.weight.dot(x)
        #print('second: ', second)

        temp = reward + first - second
        temp = self.alpha* temp * x
        #print('Temp:', temp)
        self.weight = self.weight + temp
        #print(self.state)
        #print(self.weight)
        # S = S'
        self.prevState = self.state



    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        """

        self.episode_counter +=1
        x = np.zeros(1001)

        #x[self.state] = 1
        #first = self.gamma * self.weight.dot(x)
        #print('first: ', first)

        #x[self.state] = 0
        x[self.prevState] = 1
        second =self.weight.dot(x)
        #print('second: ', second)

        temp = reward - second
        temp = self.alpha* temp * x
        #print('Temp:', temp)
        self.weight = self.weight + temp
        #print(self.state)
        #print(self.weight)





    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            return (np.max(self.Q, axis=1)).tostring()
        if in_message == 'get':
            return self.weight
        else:
            return "I dont know how to respond to this message!!"

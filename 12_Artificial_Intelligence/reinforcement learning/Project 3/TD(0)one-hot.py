from rl_glue import BaseAgent
import numpy as np
import random
from random import randint


class Agent(BaseAgent):
    """
    Monte Carlo agent -- Section 5.3 from RL book (2nd edition)

    Note: inherit from BaseAgent to be sure that your Agent class implements
    the entire BaseAgent interface
    """

    def __init__(self):
        """Declare agent variables."""
        self.alpha = None
        #self.epsilon = None
        self.actions = []
        self.state = None
        self.action = None
        self.gamma = None
        self.weight =None
        #self.prevAction= None
        self.prevState = None
        self.R = None
        self.policy = []

    def agent_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize the variables that need to be reset before each run
        begins
        """
        self.alpha = 0.5
        #self.epsilon = 0.1

        self.gamma = 1

        for i in range(70):
            #self.Q.append([0])
            #self.Q.append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

    def agent_start(self, state):
        """
        Arguments: state - numpy array
        Returns: action - integer
        Hint: Initialize the variables that you want to reset before starting
        a new episode, pick the first action, don't forget about exploring
        starts
        """
        self.state = state

        if random.uniform(0, 1) < self.epsilon:
          self.action = randint(0,7)

        else:
            self.action = np.argmax(self.Q[self.state])

        self.prevState = state
        self.prevAction = self.action

        return(self.action)

    def agent_step(self, reward, state):
        """
        Arguments: reward - floting point, state - numpy array
        Returns: action - integer
        Hint: select an action based on pi
        """
        self.R = reward
        self.state = state
        #epsilon (explore)
        '''
        if random.uniform(0, 1) < self.epsilon:
          self.action = randint(0,7)

        else:
            self.action = np.argmax(self.Q[self.state])
        '''

        temp = (self.R + (self.gamma * self.Q[self.state][self.action]) - self.Q[self.prevState][self.prevAction])
        temp = self.alpha * temp
        self.Q[self.prevState][self.prevAction] = self.Q[self.prevState][self.prevAction]+ temp


        self.prevState = self.state
        self.prevAction = self.action

        return(self.action)


    def agent_end(self, reward):
        """
        Arguments: reward - floating point
        Returns: Nothing
        Hint: do necessary steps for policy evaluation and improvement
        """
        self.R = reward
        temp = (self.R + (self.gamma * 0 - self.Q[self.prevState][self.prevAction]))
        temp = self.alpha * temp
        self.Q[self.prevState][self.prevAction] = self.Q[self.prevState][self.prevAction]+ temp



    def agent_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: The value function as a list.
        This function is complete. You do not need to add code here.
        """
        if in_message == 'ValueFunction':
            return (np.max(self.Q, axis=1)).tostring()
        else:
            return "I dont know how to respond to this message!!"

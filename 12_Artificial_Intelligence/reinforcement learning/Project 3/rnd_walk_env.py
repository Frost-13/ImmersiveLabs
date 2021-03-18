from rl_glue import BaseEnvironment
import numpy as np
import random
from random import randint


class Environment(BaseEnvironment):

    def __init__(self):
        """Declare environment variables."""
        self.start = None
        self.current_state = None
        self.R_terminate = None
        self.L_terminate = None
        self.actions = []

    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """

        self.start = 500
        self.L_terminate = 0
        self.R_terminate = 999
    def env_start(self):
        """
        Arguments: Nothing
        Returns: state - numpy array
        Hint: Sample the starting state necessary for exploring starts and return.
        """
        self.current_state = self.start
        return self.current_state

    def env_step(self, action):
        """
        Arguments: action - integer
        Returns: reward - float, state - numpy array - terminal - boolean
        Hint: Take a step in the environment based on dynamics; also checking for action validity in
        state may help handle any rogue agents.
        """
        reward = 0
        terminal = False
        state = randint(1,100)

        action = randint(0,1)
        if action == 0:
            state *= -1
        #print(self.current_state, state)
        self.current_state += state
        #print(self.current_state)

        if self.current_state <=self.L_terminate:
            reward = -1
            terminal = True
        elif self.current_state >= self.R_terminate:
            reward = 1
            terminal = True
        #print('teminal: ', terminal)
        return reward, self.current_state, terminal

    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass

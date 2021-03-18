from rl_glue import BaseEnvironment
import numpy as np


class Environment(BaseEnvironment):
    """
    Slightly modified Gambler environment -- Example 4.3 from
    RL book (2nd edition)

    Note: inherit from BaseEnvironment to be sure that your Agent class implements
    the entire BaseEnvironment interface
    """

    def __init__(self):
        """Declare environment variables."""
        self.grid = []
        self.start = None
        self.currentState = None
        self.goal = None
        self.actions = []
    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """
        self.start = 30
        self.goal = 37
        self.actions =  [-1, -11, -10, -9, 1, 9,10 , 11]
    def env_start(self):
        """
        Arguments: Nothing
        Returns: state - numpy array
        Hint: Sample the starting state necessary for exploring starts and return.
        """
        self.currentState = self.start
        return self.currentState
    def env_step(self, action):
        """
        Arguments: action - integer
        Returns: reward - float, state - numpy array - terminal - boolean
        Hint: Take a step in the environment based on dynamics; also checking for action validity in
        state may help handle any rogue agents.
        """
        temp = self.currentState
        self.currentState += self.actions[action]

        if temp%10 == 0 and self.actions[action] in [-1,-9, 9]:
            self.currentState = temp

        if temp%10 == 9 and self.actions[action] in [1, -11, 11]:
            self.currentState = temp

        if self.currentState < 0:
            self.currentState = temp

        if self.currentState > 69:
            self.currentState = temp




        reward = -1
        terminal = False



        num = self.currentState%10
        if num in [3,4,5,8]:
            #print("BLOW BY 1")
            if self.currentState >= 3 and self.currentState <= 8:
                #print("i did Nothing")
                self.currentState = self.currentState
            else:
                #print("id did blow 1")
                self.currentState -=10


        elif num in [6,7]:
            #print("BLOW BY 2")
            if self.currentState == 6 or self.currentState == 7:
                self.currentState = self.currentState
            elif self.currentState in [16,17]:
                self.currentState -= 10
            else:
                self.currentState -=20

        if self.currentState == self.goal:
            reward = 0
            terminal = True

        return reward, self.currentState, terminal

    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass

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
        grid = []
        start = None
        goal = None
        currentState = None

    def env_init(self):
        """
        Arguments: Nothing
        Returns: Nothing
        Hint: Initialize environment variables necessary for run.
        """
        self.start = 30
        self.goal = 37

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
        self.currentState += action

        if self.currentState < 0:
            self.currentState = temp

        if self.currentState > 69:
            self.currentState = temp

        # to do right hand cases
        #to do left hand cases

        wind = 0
        reward = -1
        if self.currentState == self.goal:
            reward = 1
        else:
            num = self.currentState%10:
            if num in [4,5,8]:
                self.currentState -=10
            elif num in [6,7]:
                self.currentState -=20

        return(wind, self.currentState, reward)

    def env_message(self, in_message):
        """
        Arguments: in_message - string
        Returns: response based on in_message
        This function is complete. You do not need to add code here.
        """
        pass

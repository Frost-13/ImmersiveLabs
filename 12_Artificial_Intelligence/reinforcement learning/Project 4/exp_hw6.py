#!/usr/bin/env python

import numpy as np
from agent_hw6 import Agent

from rl_glue import RLGlue
from env_hw6 import Environment
import matplotlib.pyplot as plt
import tile3 as tile



def question_1():
    # Specify hyper-parameters

    agent = Agent()
    environment = Environment()
    rlglue = RLGlue(environment, agent)

    num_episodes = 200
    num_runs = 50
    max_eps_steps = 100000

    steps = np.zeros([num_runs, num_episodes])
    for r in range(num_runs):
        print("run number : ", r)
        rlglue.rl_init()
        for e in range(num_episodes):
            rlglue.rl_episode(max_eps_steps)
            steps[r, e] = rlglue.num_ep_steps()
            #print(steps[r, e])
    np.save('steps', steps)

    # for question 2 i called plot.py after running the code above

    #Q3. im not too sure if this part works im handing it in for part marks
    # i used the algorithim from the question descripton and responses from the
    # course descripton to create the code in the agent message. however when i run
    # plot2.py it doesnt prodice any graph an i wasnt able to figure out what was wrong
    
    rlglue.rl_agent_message('Q3')

if __name__ == "__main__":
    question_1()
    print("Done")

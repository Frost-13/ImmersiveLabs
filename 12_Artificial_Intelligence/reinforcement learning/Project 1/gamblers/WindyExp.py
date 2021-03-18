import numpy as np

from WindyEnv import Environment
from WindyAgent import Agent
from rl_glue import RLGlue
import matplotlib.pyplot as plt


def experiment(rlg, num_runs, max_steps):

    rewards = np.zeros(max_steps)

    for run in range(num_runs):
        # set seed for reproducibility
        np.random.seed(run)

        # initialize RL-Glue
        rlg.rl_init()
        rlg.rl_start()

        opt = rlg.rl_env_message("msg")

        for i in range(max_steps):
            reward, state, action, is_terminal = rlg.rl_step()
            if action == opt:
                rewards[i] += 1

            #rewards[i] += reward
    #rewards /= num_runs

    rewards /= num_runs

    return rewards


def main():
    max_steps = 1000  # max number of steps in an episode --> 1000
    num_runs = 2000  # number of repetitions of the experiment --> 2000

    # Create and pass agent and environment objects to RLGlue

    #this is the epsilon optimistic approch where we explore 10% of the time
    agent = RandomAgent()
    environment = Environment1D()
    rlglue = RLGlue(environment, agent)
    del agent, environment  # don't use these anymore

    result = experiment(rlglue, num_runs, max_steps)
    #print(result)
    plt.plot(result, label = 'something', color = 'blue')

    #this is the epsilon greedy approch where we dont explore
    agent = RandomAgent2()
    environment = Environment1D()
    rlglue = RLGlue(environment, agent)
    del agent, environment  # don't use these anymore
    result = experiment(rlglue, num_runs, max_steps)
    plt.plot(result, label = 'something', color = 'red')
    plt.show()



if __name__ == '__main__':
    main()

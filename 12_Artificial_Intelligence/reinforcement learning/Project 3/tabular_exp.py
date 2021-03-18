import numpy as np

from rnd_walk_env import Environment
from tabular_agent import Agent
from rl_glue import RLGlue
import matplotlib.pyplot as plt


def experiment(val_func, rlg, num_runs, max_steps, result_plot):
    num_episodes = 2000
    # set seed for reproducibility
    np.random.seed(5)
    # initialize RL-Glue
    rlg.rl_init()
    rlg.rl_start()

    for run in range(num_runs):

        for i in range(num_episodes):
            rlg.rl_episode(max_steps)
            if(i %10) == 0:
                vk = rlg.rl_agent_message('get')

                temp = ((val_func - vk)**2).mean()
                result = np.sqrt(temp)
                result_plot.append(result)
                #print(result)
        #print('finished episode ', run)





        #print("FINISH EPISODE!!!")
        #print(result_plot)

    return result_plot


def main():
    max_steps = 2000  # max number of steps in an episode --> 2000
    num_runs = 30  # number of repetitions of the experiment --> 30
    result_plot = []
    val_func = np.load('TrueValueFunction.npy')
    agent = Agent()
    environment = Environment()
    rlglue = RLGlue(environment, agent)



    result_plot = experiment(val_func, rlglue, num_runs, max_steps, result_plot)



    plt.plot(result_plot, label = 'something', color = 'blue')
    plt.ylabel('VE')
    plt.xlabel('Episodes')
    plt.show()



if __name__ == '__main__':
    main()

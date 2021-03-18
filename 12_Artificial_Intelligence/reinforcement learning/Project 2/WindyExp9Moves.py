import numpy as np

from WindyEnv9Moves import Environment
from WindyAgent9Moves import Agent
from rl_glue import RLGlue
import matplotlib.pyplot as plt


def experiment(rlg, num_runs, max_steps):

    completed = np.zeros(max_steps)

    for run in range(num_runs):
        # set seed for reproducibility
        np.random.seed(run)

        # initialize RL-Glue
        rlg.rl_init()
        rlg.rl_start()

        epi = 0
        for i in range(max_steps):

            reward, state, action, is_terminal = rlg.rl_step()
            #print(state, action)
            if is_terminal == True:
                #print('done')
                epi+=1

                #print("FINISH!!!!")
                rlg.rl_start()

            completed[i] += epi
            #rewards[i] += reward
    completed /= num_runs


    return completed


def main():
    max_steps = 8000  # max number of steps in an episode --> 1000
    num_runs = 1  # number of repetitions of the experiment --> 2000

    # Create and pass agent and environment objects to RLGlue

    #this is the epsilon optimistic approch where we explore 10% of the time
    agent = Agent()
    environment = Environment()
    rlglue = RLGlue(environment, agent)
    #del agent, environment  # don't use these anymore
    '''environment.env_init()
    environment.env_start()

    for i in range(1000):
        action = int(input("enter an action: "))
        environment.env_step(action)
        print("State: ", environment.currentState)'''


    result = experiment(rlglue, num_runs, max_steps)
    plt.plot(result, label = 'something', color = 'red')
    plt.ylabel('Episodes')
    plt.xlabel('Time Steps')
    plt.show()



if __name__ == '__main__':
    main()

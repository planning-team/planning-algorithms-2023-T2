import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# this are the set of possible actions admitted in this problem
action_space = []
action_space.append((-1,0))
action_space.append((0,-1))
action_space.append((1,0))
action_space.append((0,1))


def plot_enviroment(env, x, goal):
    """
    env is the grid enviroment
    x is the state 
    """
    dims = env.shape    
    current_env = np.copy(env)
    # plot agent
    current_env[x] = 1.0 #yellow
    # plot goal
    current_env[goal] = 0.3
    return current_env


def state_consistency_check(env,x):
    """Checks wether or not the proposed state is a valid state, i.e. is in colision or our of bounds"""
    # check for collision
    if x[0] < 0 or x[1] < 0 or x[0] >= env.shape[0] or x[1] >= env.shape[1] :
        #print('out of bonds')
        return False
    if env[x] >= 1.0-1e-4:
        #print('Obstacle')
        return False
    return True


def transition_function(env,x,u):
    """Transition function for states in this problem
    x: current state, this is a tuple (i,j)
    u: current action, this is a tuple (i,j)
    env: enviroment
    
    Output:
    new state
    True if correctly propagated
    False if this action can't be executed
    """
    xnew = np.array(x) + np.array(u)
    xnew = tuple(xnew)
    #print('xnew',xnew)
    if state_consistency_check(env,xnew):
        return xnew, True
    return x, False


def probabilistic_transition_function(env,x,u, epsilon = 0.6):
    """Probabilistic Transition function requires:
    x: current state, this is a tuple (i,j)
    u: current action, this is a tuple (i,j)
    env: enviroment
    epsilon (in [0,1]): This is the probability of carrying out the desired action, in the extreme, 1 indicates a perfect action execution.
    
    Output:
    state_propagated_list: list of propagated states
    prob_list: list of the corresponding state's prob, in the same order
    """
    state_propagated_list = []
    prob_list = []
    for action in action_space:
        xnew = np.array(x) + np.array(action)
        xnew = tuple(xnew)
        prob = (1-epsilon)/3
        if action == u:
            prob = epsilon
        state_propagated_list.append(xnew)
        prob_list.append(prob)
    # There is no state consistency, it should be done externally when asigning the reward
    return state_propagated_list, prob_list




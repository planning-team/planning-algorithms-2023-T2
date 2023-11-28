import numpy as np
from utils import action_space, transition_function, probabilistic_transition_function, state_consistency_check

def mdp(env, goal, gamma = 0.99):
    """
    env is the grid enviroment
    goal is the goal state
    gamma: convergence hyperparamter
    
    output:
    G: Optimal cost-to-go
    """
    
    return G


def policy_mdp(env,V):
    """
    env is the grid enviroment
    V: optimal value function
    
    output:
    policy: a map from each state x to the greedy best action a to execcute
    """
    
    return policy

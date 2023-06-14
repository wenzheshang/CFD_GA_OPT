import random
from deap import base, creator, tools

def evaluate(individual):
    weights = 0
    values = 0
    # for item in individual:
    #     weights = items[item][0] + weights
    #     values = items[item][1] + values
    # if len(individual) > 15 or weights > 100:
    #     return 10000, 0
    return weights, values
    #b = len(individual)
    #return a #, b
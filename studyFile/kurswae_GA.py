from doctest import master
import random
import numpy
from deap import base, creator, tools, algorithms, benchmarks
from matplotlib import cm
from lib import cx, mut
import matplotlib.pyplot as plt
import numpy as np


def main():
    IND_size = 2
    # MIN = -10
    # MAX = 10
    random.seed(64)

    creator.create('FitnessMin', base.Fitness, weights = (-1.0, -1.0)) #kurswae function co-Minmize
    creator.create('Individual', list, fitness = creator.FitnessMin)

    def randomlist():
        return random.uniform(-5,5)

    toolbox = base.Toolbox()
    toolbox.register('attr_item', randomlist)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_item, n = IND_size)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    def evaluate(individual):

        X, Y = (individual[0], individual[0])

        Z1 = np.array([0])
        Z2 = np.array([0])

        Z1,  Z2 = benchmarks.fonseca((X, Y))

        return Z1, Z2

    toolbox.register("evaluate", evaluate)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selNSGA2)

    # toolbox.decorate("mate", decorate.checkBounds(MIN, MAX))
    # toolbox.decorate("mutate", decorate.checkBounds(MIN, MAX))

    mstats = tools.Statistics(key=lambda ind: ind.fitness.values)
    mstats.register('avg', numpy.mean, axis = 0)
    mstats.register('std', numpy.std, axis = 0)
    mstats.register('min', numpy.min, axis = 0)
    mstats.register('max', numpy.max, axis = 0)

    CXPB = 0.7
    MUTPB = 0.2
    NGEN = 200
    MU = 50
    LAMBDA = 100

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, mstats,
                              halloffame=hof)

    return pop, mstats, hof

if __name__=='__main__':
    (p, sta, hof) = main()
    i = 0
    gen = []
 
    positionX = []
    positionY = []

    for ind in hof:
        i += 1
        
        positionX += [ind[0]]
        positionY += [ind[1]]

        gen += [i]
    
    PX, PY = np.meshgrid(positionX, positionY)
    Z1 = np.zeros(PX.shape)
    Z2 = np.zeros(PX.shape)
    fit_Z1 = []
    fit_Z2 = []

    for i in range(PX.shape[0]):
        for j in range(PX.shape[1]):
            Z1[i,j],  Z2[i,j] = benchmarks.fonseca((PX[i,j], PY[i,j]))
    
    for ind in hof:
        fit_Z1 += [ind.fitness.values[0]]
        fit_Z2 += [ind.fitness.values[1]]

    fig = plt.figure(figsize=(18,5))

    ax0 = fig.add_subplot(1, 3, 1, projection='3d')
    ax0.scatter(PX, PY, Z1, label="Z1 Paerto front")
    ax0.set_xlabel("x")
    ax0.set_ylabel("y")

    ax1 = fig.add_subplot(1, 3, 2, projection='3d')
    ax1.scatter(PX, PY, Z2, label="Z2 Paerto front")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")

    ax2 = fig.add_subplot(1, 3, 3)
    line1 = ax2.plot(fit_Z1, fit_Z2, "b-", label="KnapsackP Paerto front")
    ax2.set_xlabel("Z1")
    ax2.set_ylabel("Z2", color="b")
    for tl in ax2.get_yticklabels():
        tl.set_color("b")

    lns = line1
    labs = [l.get_label() for l in lns]
    ax2.legend(lns, labs, loc="center right")


    plt.show()
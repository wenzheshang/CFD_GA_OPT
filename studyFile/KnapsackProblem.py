from doctest import master
import random
import numpy
from deap import base, creator, tools, algorithms
from lib import cx, mut, CFD
import matplotlib.pyplot as plt


def main():
    IND_size = 5
    NBR_ITEMS = 20
    # MIN = -10
    # MAX = 10
    random.seed(64)

    creator.create('FitnessMax', base.Fitness, weights = (-1.0, 1.0))
    creator.create('Individual', list, fitness = creator.FitnessMax)

    items = {}
    
    for i in range(NBR_ITEMS):
        items[i] = (random.randint(1, 10), random.uniform(0, 100))#(weights, values)
    
    #CFD.CFD_simu('case_name', velocity=items['0'])

    toolbox = base.Toolbox()
    toolbox.register('attr_item', random.randrange, NBR_ITEMS)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_item, n = IND_size)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    def evaluate(individual):
        weights = 0
        values = 0
        for item in individual:
            weights += items[item][0]
            values += items[item][1]
        if len(individual) > 50 or weights > 50:
            return 10000, 0
        return weights, values

    toolbox.register("evaluate", evaluate)
    toolbox.register('mate', tools.cxTwoPoint)#cx.cxSet)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)#mut.mutSet)
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
    fit_weight = []
    fit_values = []

    for ind in hof:
        i += 1
        fit_weight += [ind.fitness.values[0]]
        fit_values += [ind.fitness.values[1]]
        gen += [i]

    fig, ax1 = plt.subplots()
    line1 = ax1.plot(fit_weight, fit_values, "b-", label="KnapsackP Paerto front")
    ax1.set_xlabel("Weight")
    ax1.set_ylabel("Values", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    lns = line1
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    plt.show()
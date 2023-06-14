import random
import lib.initPop
import lib.evaluate
#import decorate
import numpy
from deap import base, creator, tools

def main():
    IND_size = 100
    # MIN = -10
    # MAX = 10

    creator.create('FitnessMax', base.Fitness, weights = (1.0,))
    creator.create('Individual', list, fitness = creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register('attr_bool', random.randint, 0, 1)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_bool, n = IND_size)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", lib.evaluate.evaluate)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # toolbox.decorate("mate", decorate.checkBounds(MIN, MAX))
    # toolbox.decorate("mutate", decorate.checkBounds(MIN, MAX))

    stats_fit = tools.Statistics(key=lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(key=len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register('avg', numpy.mean)
    mstats.register('std', numpy.std)
    mstats.register('sum', numpy.sum)
    mstats.register('max', numpy.max)


    pop = toolbox.population(n = 300)
    fitness = list(map(toolbox.evaluate, pop))
    
    for ind, fit in zip(pop, fitness):
        ind.fitness.values = [fit]

    CXPB = 0.5
    MUTPB = 0.2
    NGEN = 1000

    fits = [ind.fitness.values[0] for ind in pop]
    g = 0

    logbook = tools.Logbook()

    while max(fits) < 100 and g < NGEN:
        g = g + 1
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        # Apply mutation on the offspring
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = [fit]

        # The population is entirely replaced by the offspring
        pop[:] = offspring

        record = mstats.compile(pop)


        logbook.record(gen=g, evals=30, **record)

    logbook.header = "gen", "evals", "fitness", "size"
    logbook.chapters["fitness"].header = "min", "avg", "max"
    logbook.chapters["size"].header = "min", "avg", "max"    

    gen = logbook.select("gen")
    fit_sum = logbook.chapters['fitness'].select("max")
    size_avgs = logbook.chapters['fitness'].select("avg")

    import matplotlib.pyplot as plt

    fig, ax1 = plt.subplots()
    line1 = ax1.plot(gen, fit_sum, "b-", label="Max Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")
    for tl in ax1.get_yticklabels():
        tl.set_color("b")

    ax2 = ax1.twinx()
    line2 = ax2.plot(gen, size_avgs, "r-", label="Average fitness")
    ax2.set_ylabel("Size", color="r")
    for tl in ax2.get_yticklabels():
        tl.set_color("r")

    lns = line1 + line2
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, loc="center right")

    plt.show()

if __name__=='__main__':
    main()


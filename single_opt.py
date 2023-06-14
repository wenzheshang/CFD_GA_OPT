from deap import base, creator, tools, algorithms
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import random
import matplotlib.pyplot as plt
import numpy
import time

X_BOUND = [-2.048, 2.048]
Y_BOUND = [-2.048, 2.048]

class CallingCounter(object):
    def __init__ (self, func):
        self.func = func
        self.count = 0

    def __call__ (self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

def F(x, y):
    return 100.0 * (y - x ** 2.0) ** 2.0 + (1 - x) ** 2.0

def main():
    IND_size = 2

    creator.create('FitnessMax', base.Fitness, weights = (1.0,))
    creator.create('Individual', list, fitness = creator.FitnessMax)

    toolbox = base.Toolbox()
    toolbox.register('attr_item', random.uniform, -2.048, 2.048)
    toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.attr_item, n = IND_size)
    toolbox.register('population', tools.initRepeat, list, toolbox.individual)

    @CallingCounter
    def evaluate(individual):
        z = 100.0 * (individual[1] - individual[0] ** 2.0) ** 2.0 + (1 - individual[0]) ** 2.0
        print("test times:" f'{evaluate.count}')
        time.sleep(1)
        return [z]

    toolbox.register("evaluate", evaluate)
    toolbox.register('mate', tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)
    toolbox.register("select", tools.selTournament, tournsize=3)

    MU = 50

    pop = toolbox.population(n=MU)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100)

    return pop

def plot_3d(ax):
    X = numpy.linspace(*X_BOUND, 100)
    Y = numpy.linspace(*Y_BOUND, 100)
    X, Y = numpy.meshgrid(X, Y)
    Z = F(X, Y)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

if __name__=='__main__':
    p = main()
    
    fig = plt.figure()
    
    ax1 = fig.add_subplot(1, 1, 1, projection='3d')
    plot_3d(ax1)
    
    x = p[0][0]
    y = p[0][1]
    sca = ax1.scatter(x, y, F(x, y), c='black', marker='o')
    plt.show()

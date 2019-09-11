import pylab as pl
import numpy as np
from SGA import *

def getCategory(arr):
    return 4 * arr[0] + 2 * arr[1] + arr[2]

def getFitness(chrome):
    fitDict = {'Sarah': {0: 10, 1: 5, 2: 4, 3: 6, 4: 5, 5: 1, 6 : 0, 7: 0},
                    'Jessica': {0: 6, 1: 4, 2: 9, 3: 7, 4: 3, 5: 2, 6 : 0, 7: 0},
                    'George': {0: 1, 1: 8, 2: 3, 3: 6, 4: 4, 5: 6, 6 : 0, 7: 0},
                    'Karen': {0: 5, 1: 3, 2: 7, 3: 2, 4: 1, 5: 4, 6 : 0, 7: 0},
                    'Sam': {0: 3, 1: 2, 2: 5, 3: 6, 4: 8, 5: 7, 6 : 0, 7: 0},
                    'Tim': {0: 7, 1: 6, 2: 4, 3: 1, 4: 3, 5: 2, 6 : 0, 7: 0}}
    cats = [getCategory(chrome[0:3]), getCategory(chrome[3:6]), getCategory(chrome[6:9]), getCategory(chrome[9:12]), getCategory(chrome[12:15]) ,getCategory(chrome[15:18])]
    return cats, fitDict['Sarah'][cats[0]] + fitDict['Jessica'][cats[1]] + fitDict['George'][cats[2]] + \
        fitDict['Karen'][cats[3]] + fitDict['Sam'][cats[4]] + fitDict['Tim'][cats[5]]

def runTest(size, population, generations, pm, pc, exponent):
    runs = 20
    test = sga(size, population, generations, pm, pc, exponent)
    currBestFit = 0
    currBestChromesome = []
    for i in range(0, runs):
        tb, ta = test.runGA()
        if tb > currBestFit:
            currBestFit = tb
            currBestChromesome = ta
    return getFitness(currBestChromesome), currBestChromesome

size = 18
population = 100
generations = 21
range_size = 15

# These lines are for testing different values for the probability of mutations, probability of crossover, and exponent used in the fitness function
# ranges = range(0, range_size)
# pmArr = [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009]
# pcArr = [0.7, 0.75, 0.8, 0.85, 0.9]
# exponentArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# bestPms, bestPmFit = {}, 0
# bestPcs, bestPcFit = {}, 0
# bestExponents, bestExponentFit = {}, 0


# for pm in pmArr:
#     tempFit = 0
#     for i in ranges:
#         tempFit += runTest(size, population, generations, pm, pcArr[int(len(pcArr)/2)], exponentArr[int(len(exponentArr)/2)])[1]
#     tempFit = tempFit / range_size
#     bestPms[pm] = tempFit

# for pc in pcArr:
#     tempFit = 0
#     for i in ranges:
#         tempFit += runTest(size, population, generations, pmArr[int(len(pcArr)/2)], pc, exponentArr[int(len(exponentArr)/2)])[1]
#     tempFit = tempFit / range_size
#     bestPcs[pc] = tempFit

# for exponent in exponentArr:
#     tempFit = 0
#     for i in ranges:
#         tempFit += runTest(size, population, generations, pmArr[int(len(pcArr)/2)], pcArr[int(len(pcArr)/2)], exponent)[1]
#     tempFit = tempFit / range_size
#     bestExponents[exponent] = tempFit

# print("The best pm(s) found are: " + str(bestPms) + ", the best pm(s) found are: " + str(bestPcs) + ", the best pm(s) found are: " + str(bestExponents))

# These values for pm, pc, and exponent were determined using the code above
pm = 0.009
pc = 0.875
exponent = 6
categoryDict = {0 : 'Geology', 1 : 'Physics', 2 : 'Chemistry', 3 : 'History', 4 : 'Poetry', 5 : 'Art'}
[categories, maxFitness], bestChromesome = runTest(size, population, generations, pm, pc, exponent)
print("The most fit chromesome found is " + str(bestChromesome) + " which has a fitness of " + str(maxFitness) + " resulting in Sarah categorizing " + categoryDict[categories[0]] + \
    ", Jessica categorizing " + categoryDict[categories[1]] + ", George categorizing " + categoryDict[categories[2]] + ", Karen categorizing " + categoryDict[categories[3]] + \
        ", Sam categorizing " + categoryDict[categories[4]] + ", and Tim categorizing " + categoryDict[categories[5]] + ".")

# [0 0 0, 0 1 1, 1 0 1, 0 1 0, 1 0 0, 0 0 1] at locn 0, fitness: 44.0


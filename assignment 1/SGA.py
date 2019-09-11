# Simple Genetic Algorithm

import pylab as pl
import numpy as np


class sga:

   def __init__(self, stringLength, popSize, nGens, pm, pc, exponent):
      # stringLength: int, popSize: int, nGens: int,
      # prob. mutation pm: float; prob. crossover pc: float
      fid = open("results.txt", "w")        # open, initialize output file
      self.fid = fid
      self.stringLength = stringLength
      if np.mod(popSize, 2) == 0:           # popSize must be even
         self.popSize = popSize
      else:
	      self.popSize = popSize+1
      self.pm = pm                       # prob of mutation
      self.pc = pc                       # prob of crossover
      self.nGens = nGens                 # max num generations
      self.pop = np.random.rand(self.popSize, self.stringLength)
      self.pop = np.where(self.pop < 0.5, 1, 0)  # create initial pop
      self.fitDict = {'Sarah': {0: 10, 1: 5, 2: 4, 3: 6, 4: 5, 5: 1, 6 : 0, 7: 0},
                    'Jessica': {0: 6, 1: 4, 2: 9, 3: 7, 4: 3, 5: 2, 6 : 0, 7: 0},
                    'George': {0: 1, 1: 8, 2: 3, 3: 6, 4: 4, 5: 6, 6 : 0, 7: 0},
                    'Karen': {0: 5, 1: 3, 2: 7, 3: 2, 4: 1, 5: 4, 6 : 0, 7: 0},
                    'Sam': {0: 3, 1: 2, 2: 5, 3: 6, 4: 8, 5: 7, 6 : 0, 7: 0},
                    'Tim': {0: 7, 1: 6, 2: 4, 3: 1, 4: 3, 5: 2, 6 : 0, 7: 0}}
      self.exponent = exponent
      fitness = self.fitFcn(self.pop)    # fitness values for initial population
      self.bestfit = fitness.max()       # fitness of (first) most fit chromosome
      self.bestloc = np.where(fitness == self.bestfit)[0][0]  # most fit chromosome locn
      self.bestchrome = self.pop[self.bestloc,:]              # most fit chromosome
      # array of max fitness vals each generation
      self.bestfitarray = np.zeros(self.nGens + 1)
      self.bestfitarray[0] = self.bestfit  # (+ 1 for init pop plus nGens)
      # array of mean fitness vals each generation
      self.meanfitarray = np.zeros(self.nGens + 1)
      self.meanfitarray[0] = fitness.mean()
      fid.write("popSize: {}  nGens: {}  pm: {}  pc: {}\n".format(popSize, nGens, pm, pc))
      fid.write("initial population, fitnesses: (up to 1st 100 chromosomes)\n")
      for c in range(min(100, popSize)):   # for each of first 100 chromosomes
         fid.write("  {}  {}\n".format(self.pop[c, :], fitness[c]))
      fid.write("Best initially:\n  {} at locn {}, fitness = {}\n".format(
         self.bestchrome, self.bestloc, self.bestfit))

  # to be modified ---------------------vvvvvv
   def calcFitness(self, chrome):
      sarah = 4*chrome[0] + 2*chrome[1] + chrome[2]
      jessica = 4*chrome[3] + 2*chrome[4] + chrome[5]
      if jessica == sarah:
         return 0
      george = 4*chrome[6] + 2*chrome[7] + chrome[8]
      if jessica == george or george == sarah:
         return 0
      karen = 4*chrome[9] + 2*chrome[10] + chrome[11]
      if jessica == karen or karen == sarah or karen == george:
         return 0
      sam = 4*chrome[12] + 2*chrome[13] + chrome[14]
      if jessica == sam or sam == sarah or sam == george or sam == karen:
         return 0
      tim = 4*chrome[15] + 2*chrome[16] + chrome[17]
      if jessica == tim or tim == sarah or tim == george or tim == karen or tim == sam:
         return 0
      return self.fitDict['Sarah'][sarah]**self.exponent + self.fitDict['Jessica'][jessica]**self.exponent  + self.fitDict['George'][george]**self.exponent \
         + self.fitDict['Karen'][karen]**self.exponent  + self.fitDict['Sam'][sam]**self.exponent  + self.fitDict['Tim'][tim]**self.exponent 

   def fitFcn(self, pop):          
      # compute population fitness values
      fitness = np.zeros(self.popSize)
      for i in range(0, self.popSize):
         fitness[i] = self.calcFitness(pop[i])
      return fitness

   # end modifications ------------------^^^^^^

  # conduct tournaments of size 2 twice to select two offspring
   def tournament(self, pop, fitness, popsize):  # fitness array, pop size
      # select first parent par1
      cand1 = np.random.randint(popsize)      # candidate 1, 1st tourn., int
      cand2 = cand1                           # candidate 2, 1st tourn., int
      while cand2 == cand1:                   # until cand2 differs
        cand2 = np.random.randint(popsize)  # identify a second candidate
      if fitness[cand1] > fitness[cand2]:     # if cand1 more fit than cand2
        par1 = cand1  # then first parent is cand1
      else:  # else first parent is cand2
        par1 = cand2
     # select second parent par2
      cand1 = np.random.randint(popsize)      # candidate 1, 2nd tourn., int
      cand2 = cand1                           # candidate 2, 2nd tourn., int
      while cand2 == cand1:                   # until cand2 differs
        cand2 = np.random.randint(popsize)  # identify a second candidate
      if fitness[cand1] > fitness[cand2]:     # if cand1 more fit than cand2
        par2 = cand1  # then 2nd parent par2 is cand1
      else:  # else 2nd parent par2 is cand2
        par2 = cand2
      return par1, par2

   def xover(self, child1, child2):    # single point crossover
      # cut locn to right of position (hence subtract 1)
      locn = np.random.randint(0, self.stringLength - 1)
      tmp = np.copy(child1)       # save child1 copy, then do crossover
      child1[locn+1:self.stringLength] = child2[locn+1:self.stringLength]
      child2[locn+1:self.stringLength] = tmp[locn+1:self.stringLength]
      return child1, child2


   def mutate(self, pop):            # bitwise point mutations
        whereMutate = np.random.rand(np.shape(pop)[0], np.shape(pop)[1])
        whereMutate = np.where(whereMutate < self.pm)
        pop[whereMutate] = 1 - pop[whereMutate]
        return pop


   def runGA(self):     # run simple genetic algorithme
    fid = self.fid   # output file
    for gen in range(self.nGens):  # for each generation gen
        # Compute fitness of the pop
        fitness = self.fitFcn(self.pop)  # measure fitness
        # initialize new population
        newPop = np.zeros((self.popSize, self.stringLength), dtype='int64')
        # create new population newPop via selection and crossovers with prob pc
        for pair in range(0, self.popSize, 2):  # create popSize/2 pairs of offspring
            # tournament selection of two parent indices
            p1, p2 = self.tournament(
                self.pop, fitness, self.popSize)  # p1, p2 integers
            child1 = np.copy(self.pop[p1, :])       # child1 for newPop
            child2 = np.copy(self.pop[p2, :])       # child2 for newPop
            if np.random.rand() < self.pc:                 # with prob self.pc
                child1, child2 = self.xover(child1, child2)  # do crossover
            newPop[pair, :] = child1                # add offspring to newPop
            newPop[pair + 1, :] = child2
        # mutations to population with probability pm
        newPop = self.mutate(newPop)
        self.pop = newPop
        # fitness values for initial population
        fitness = self.fitFcn(self.pop)
        self.bestfit = fitness.max()       # fitness of (first) most fit chromosome
        # save best fitness for plotting
        self.bestfitarray[gen + 1] = self.bestfit
        # save mean fitness for plotting
        self.meanfitarray[gen + 1] = fitness.mean()
        self.bestloc = np.where(fitness == self.bestfit)[
            0][0]  # most fit chromosome locn
        self.bestchrome = self.pop[self.bestloc,
                                   :]              # most fit chromosome
   # If running to test for best values of pm, pc, and exponent, comment from this line
        if (np.mod(gen, 10) == 0):            # print epoch, max fitness
            print("generation: ", gen+1, "max fitness: ", self.bestfit)
    fid.write("\nfinal population, fitnesses: (up to 1st 100 chromosomes)\n")
    # To this line
    fitness = self.fitFcn(self.pop)         # compute population fitnesses
    self.bestfit = fitness.max()            # fitness of (first) most fit chromosome
    self.bestloc = np.where(fitness == self.bestfit)[
        0][0]  # most fit chromosome locn
    self.bestchrome = self.pop[self.bestloc,
                               :]              # most fit chromosome
   
   # If running to test for best values of pm, pc, and exponent, or runs != 1, comment from this line
   #  for c in range(min(100, self.popSize)):  # for each of first 100 chromosomes
   #      fid.write("  {}  {}\n".format(self.pop[c, :], fitness[c]))
   #  fid.write("Best:\n  {} at locn {}, fitness: {}\n\n".format(
   #      self.bestchrome, self.bestloc, self.bestfit))
   #  pl.ion()      # activate interactive plotting
   #  pl.xlabel("Generation")
   #  pl.ylabel("Fitness of Best, Mean Chromosome")
   #  pl.plot(self.bestfitarray, 'kx-', self.meanfitarray, 'kx--')
   #  pl.show()
   #  pl.pause(0)
   #  fid.close()
   # To this line
    return self.bestfit, self.bestchrome

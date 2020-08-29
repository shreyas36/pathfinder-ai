import numpy as np
import random

population= 10
steps =10
mutationrate=5

fitness= [0]*population
parents = np.random.randint(1,5,(population,steps))

def matingpool(fitness):
	matpool=[]
	for i in range(population):
		matpool+=[i]*fitness[i]
	return matpool

def stepincrease(size):
	for parent in parents:
		addition = np.random.randint(1,5,(1,5))[0]
		parent+=addition

def crossover(matpool,parents):
	midpoint = random.choice(1,steps)
	a=10
	newparents=[]
	while a>0:
		a-=1
		parent1=random.choice(matpool)
		parent2=random.choice(matpool)
		child=[]
		i=0
		while i<midpoint:
			child.append(parents[parent1][i])
            i+=1
        while i<steps:
            child.append(parents[parent2][i])
            i+=1
        newparents.append(child)
    return newparents

def mutate(children):
	for j in range(population):
        for i in range(steps):
            if random.randint(1,100)<mutationrate:
                pop[j][i]=random.randint(1,4)

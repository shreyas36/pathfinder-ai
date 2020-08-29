import random


population=10
steps=10
mutationrate=5
pop=[0]*population

#intial generatioin
for i in range(population):
    pop[i]=[0]
    for j in range(steps-1):
        pop[i].append(j)

fitnes=[0]*population

#random entries in population
for i in range(population):
    for j in range(steps):
        pop[i][j]=random.randint(1,4)


#adjustment to each list in population on step increase
def stepincrease(size):
    addition=[]
    for j in range(size):
        addition.append(random.randint(1,4))
    for parent in pop:
        parent=parent+addition

#mating pool in which each parent is added number of times its fitness score
def matingpool(fitnes):
    m=[]
    for i in range(population):
        for j in range(fitnes[i]):
            m.append([i,0])
    return m

#random two parents in matpool cutoff at random midpt and joined to create child
def crossover(matpool,pop):
    midpoint=random.randint(1,steps)
    a=10
    newpop=[]
    while a>0:
        a-=1
        p1=random.choice(matpool)
        matpool[p1[0]][1]=1
        p2=[0,1]
        while p2[1]!=0:
            p2=random.choice(matpool)
        child=[]
        i=0
        while i<midpoint:
            child.append(pop[p1[0]][i])
            i+=1
        while i<steps:
            child.append(pop[p2[0]][i])
            i+=1
        newpop.append(child)
    return newpop

#newpop=crossover(mpool,pop)
#to add randomness in children
def mutate(pop):
    for j in range(population):
        for i in range(steps):
            if random.randint(1,100)<mutationrate:
                pop[j][i]=random.randint(1,4)

#mpool=matingpool(fitnes)
#print(mpool)

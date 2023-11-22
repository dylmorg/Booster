import os
import random 
import re 

cubeFile = "cube.txt"
packSize = 15

bonusPack = []
data = []
poolList = []
with open(cubeFile) as cubeList:
    for val in cubeList.readlines():
        val = val.strip('\n')
        if  not val.startswith("# ") and len(val) > 0:
            val = val.strip('\n')
            data.append(val) 

print (data)
for pool in os.listdir():
    if pool.endswith(".txt") and not pool.startswith(cubeFile):
        poolList.append(pool)

for pool in poolList:  
    with open (pool) as currentPool:
        for currentCard in currentPool.readlines():
            if (currentCard.find("\d ")):
                currentCard =  re.sub("\d ", "", currentCard)
                print(currentCard)
                if (currentCard in data):
                    data.remove(currentCard)
print (data)

for i in range (1, packSize):
    chosenCard = random.choice(data)
    print(chosenCard)
    bonusPack.append(chosenCard)
    data.remove(chosenCard)

print (bonusPack)
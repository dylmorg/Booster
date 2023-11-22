import os
import random 

cubeFile = "cube.txt"
packSize = 15

bonusPack = []
data = []
poolList = [] 
with open(cubeFile) as cubeList:
    for val in cubeList.readlines():
        if val and val !="# mainboard" and val !="# sideboard" and val != "# maybeboard" and val != '':
            val = val.strip('\n')
            data.append(val) 


for pool in os.listdir():
    if pool.endswith(".txt") and not pool.startswith(cubeFile):
        poolList.append(pool)

for pool in poolList:
    with open (pool) as currentPool:
        for currentCard in currentPool.readlines():
            currentCard = currentCard.strip('\n')
            currentCard = currentCard.strip('1 ')
            print (currentCard)
            if (currentCard in data):
                print (currentCard)
                data.remove(currentCard)
print (data)

for i in range (1, packSize):
    chosenCard = random.choice(data)
    print(chosenCard)
    bonusPack.append(chosenCard)
    data.remove(chosenCard)

print (bonusPack)
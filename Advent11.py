import numpy as np
import cProfile

def ReadFile(fname):
    with open(fname, "r") as file:
        my_data = [[int(val) for val in line.split()] for line in file][0]
    return my_data

def Blink(stones):
    newstones = []
    for stone in stones:
        if stone == 0:
            newstones.append(1)
            continue
        strStone = str(stone)
        lenStone = len(strStone)
        if (lenStone%2 == 0):
            midindex = int(lenStone/2)
            if midindex == 0:
                newstones.append(int(strStone[0]))
                newstones.append(int(strStone[1]))
            else:
                newstones.append(int(strStone[0:midindex]))
                newstones.append(int(strStone[midindex:]))
            continue
        newstones.append(stone*2024)
    return newstones

def recHowManyStonesAfterBlinks(stone, numberOfBlinks):
    
    

    if numberOfBlinks == 0:
        return 1

    if stone == 0:
        return recHowManyStonesAfterBlinks(1, numberOfBlinks -1)

    strStone = str(stone)
    lenStone = len(strStone)
    if (lenStone%2 == 0):
        midindex = int(lenStone/2)
        if midindex == 0:
            return recHowManyStonesAfterBlinks(int(strStone[0]), numberOfBlinks -1) + recHowManyStonesAfterBlinks(int(strStone[1]), numberOfBlinks -1) 
        else:
            return recHowManyStonesAfterBlinks(int(strStone[0:midindex]), numberOfBlinks -1) + recHowManyStonesAfterBlinks(int(strStone[midindex:]), numberOfBlinks -1)
    
    return recHowManyStonesAfterBlinks(stone * 2024, numberOfBlinks -1)

def BlinkSeveralTimes(stones, number):
    for i in range(number):
        stones = Blink(stones)
        deciles = np.quantile(stones, q=[0.9, 0.99])
        print(deciles)
    return stones

def PrintSum(blinks):
    stones = ReadFile("Advent11inputdummy.txt")
    print(sum([recHowManyStonesAfterBlinks(val, blinks) for val in stones]))


#print(stones)
#blink25Times = BlinkSeveralTimes([0], 25)

cProfile.run('PrintSum(40)')

#blink50Times = [BlinkSeveralTimes([stone], 25) for stone in blink25Times]
#sum50 = [sum(line) for line in blink50Times]
#print(sum(sum50))


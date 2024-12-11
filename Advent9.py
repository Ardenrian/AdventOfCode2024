import copy

def ReadFile(fname):
    with open(fname, "r") as file:
        my_data = [[int(char) for char in line if not(char == '\n')] for line in file][0]
    return my_data

def WriteBlocks(diskMap):
    blocks=[]
    isFile = True
    index = 0
    for size in diskMap:
        if not(isFile):
            blocks.extend([-1]*size)
        else:
            blocks.extend([index]*size)
            index = index+1
        isFile = not(isFile)
    return blocks

def MoveBlocksOneByOne(blocks):
    movedBlocks = copy.copy(blocks)
    indexToSwap = -1
    for i,e in reversed(list(enumerate(movedBlocks))):
        if e > -1:
            indexToSwap = next((i for (i,e2) in enumerate(movedBlocks) if (e2 == -1)), -1) #can be optimized obv
            if indexToSwap < i:
                movedBlocks[indexToSwap] = e
                movedBlocks[i]=-1
    return movedBlocks

def WriteSmartBlocks(my_data):
    smartBlocks = []
    indexInBlocks = 0
    indexInFiles = 0
    isFile = True
    for number in my_data:
        if isFile:
            smartBlocks.append([indexInBlocks, number, indexInFiles])
            indexInFiles = indexInFiles + 1
        indexInBlocks = indexInBlocks + number
        isFile = not(isFile)
    return smartBlocks

def MoveWholeBlock(smartBlocks):
    smartBlocksMoved = copy.copy(smartBlocks)
    
    for i, b in reversed(list(enumerate(smartBlocks))):
        for (ni, nb) in enumerate(smartBlocksMoved):
            if b[0] == nb[0]:
                break
            if ni == len(smartBlocksMoved)-1:
                break
            if smartBlocksMoved[ni+1][0] >= (nb[0] + nb[1] + b[1]):
                newElement = copy.copy(b)
                newElement[0] = nb[0] + nb[1]
                smartBlocksMoved.insert(ni+1, newElement)
                smartBlocksMoved.remove(b)
                break
    return smartBlocksMoved

def BuildBlocks(smartBlocks):
    builtBlocks = [-1]*(smartBlocks[-1][0] + smartBlocks[-1][1])
    for block in smartBlocks:
        for i in range(block[1]):
            builtBlocks[i+block[0]] = block[2]
    return builtBlocks

my_data = ReadFile("Advent9input.txt")
print(my_data)
blocks = WriteBlocks(my_data)
print(blocks)
#movedBlocks = MoveBlocksOneByOne(blocks)
#print(movedBlocks)
#print(sum([i*e for (i,e) in enumerate(movedBlocks) if e>-1]))

smartBlocks = WriteSmartBlocks(my_data)
print(smartBlocks)
smartBlocksMoved = MoveWholeBlock(smartBlocks)
print(smartBlocksMoved)
builtBlocks = BuildBlocks(smartBlocksMoved)
print(builtBlocks)
print(sum([i*e for (i,e) in enumerate(builtBlocks) if e>-1]))
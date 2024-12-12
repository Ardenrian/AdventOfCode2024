from tabulate import tabulate
import copy

def ReadFile(fname):
    with open(fname, "r") as file:
        lines = [[int(char) for char in line if not(char == '\n')] for line in file]
    return lines

def CreateQuarternaryList(number):
    quarternaryList = [int(number/pow(4,i))%4 for i in range(8)]
    return quarternaryList

def GenerateAllPossibleQuarternaries():
    quarternaries = [CreateQuarternaryList(i) for i in range(pow(4,8))]
    return quarternaries

def NextCoord(i, j, dir):
    if dir == 0:
        return (i-1, j)
    if dir == 1:
        return (i+1,j)
    if dir == 2:
        return (i, j-1)
    if dir == 3:
        return (i, j+1)

def IsInside(listList, i, j):
    if i >-1 :
        if j >-1 :
            if i < len(listList):
                if j < len(listList[0]):
                    return True
    return False

def Process(topoMap, tuple):
    tuplesToAdd = []
    mountainTopsToAdd = []

    for dir in range(4):
        (i,j) = NextCoord(tuple[0], tuple[1], dir)
        if IsInside(topoMap, i, j):
            if topoMap[i][j] == tuple[2] + 1:
                if tuple[2] == 8:
                    mountainTopsToAdd.append((i,j))
                else:
                    tuplesToAdd.append((i,j,tuple[2]+1))
    return (tuplesToAdd, mountainTopsToAdd)

def AddWithoutDuplicate(list1, list2):
    for it in list2:
        if it in list1:
            continue
        list1.append(it)
    return list1

def HowManyFromCoords(topoMap, i, j, withHistory):
    mountainTops = []    
    if not(topoMap[i][j] == 0):
        return 0
    
    ''' the brute force way, which is too heavy even on the dummy input lol
    for quaternary in quaternaries:
        ic = i
        jc = j
        for (dir, index) in enumerate(quaternary):
            (ic,jc) = NextCoord(ic, jc, dir)
            if not(IsInside(topoMap, ic, jc)):
                break
            if not(topoMap[ic][jc] == ic + 1):
                break
            if (index == 8):
                if not((ic,jc) in mountainTops):
                    mountainTops.append((ic,jc))
    '''
    listToProcess = [(i,j,0)]

    while len(listToProcess) > 0:
        (tuplesToAdd, mountainTopsToAdd) = Process(topoMap, listToProcess.pop())
        if (withHistory):
            listToProcess = listToProcess + tuplesToAdd
            mountainTops = mountainTops + mountainTopsToAdd
        else:
            listToProcess = AddWithoutDuplicate(listToProcess, tuplesToAdd)
            mountainTops = AddWithoutDuplicate(mountainTops, mountainTopsToAdd)

    return len(mountainTops)

topoMap = ReadFile("Advent10input.txt")
print(tabulate(topoMap))
trailheads = [[HowManyFromCoords(topoMap, j, i, 1) for i in range(len(topoMap[0]))] for j in range(len(topoMap))]
print(tabulate(trailheads))
print(sum([sum(line) for line in trailheads]))
from enum import Enum
import re

def ReadFile(fname):
    file = open(fname, "r")
    lines = [line for line in file]
    file.close()
    return lines

def getNeighbour(i, j, dir, step): #dir is a string
    if (re.search('U', dir)):
        i = i+step
    if (re.search('D', dir)):
        i = i-step
    if (re.search('L', dir)):
        j = j-step
    if (re.search('R', dir)):
        j = j+step
    return (i,j)

def IsXMAS(lines,i,j,dir):
    if (lines[i][j] != 'X'):
        return False
    sneigh = getNeighbour(i,j,dir,3)
    if (sneigh[0]<0) | (sneigh[1]<0) | (sneigh[0]>(len(lines)-1)) | (sneigh[1]>(len(lines[0])-1)):
        return False
    aneigh = getNeighbour(i,j,dir,2)
    mneigh = getNeighbour(i,j,dir,1)
    if (lines[sneigh[0]][sneigh[1]]=='S') & (lines[aneigh[0]][aneigh[1]]=='A') & (lines[mneigh[0]][mneigh[1]]=='M'):
        return True
    return False

def IsX_MAS(lines, i, j):
    if (lines[i][j] != 'A'):
        return False
    if (i-1<0) | (j-1<0) | (i+1>(len(lines)-1)) | (j+1>(len(lines[0])-1)):
        return False
    neighUL = getNeighbour(i,j,'UL',1)
    neighUR = getNeighbour(i,j,'UR',1)
    neighDL = getNeighbour(i,j,'DL',1)
    neighDR = getNeighbour(i,j,'DR',1)
    sul = lines[neighUL[0]][neighUL[1]]
    sur = lines[neighUR[0]][neighUR[1]]
    sdl = lines[neighDL[0]][neighDL[1]]
    sdr = lines[neighDR[0]][neighDR[1]]

    if ((sul == 'M') & (sur == 'M') & (sdl == 'S') & (sdr == 'S')) | ((sul == 'M') & (sur == 'S') & (sdl == 'M') & (sdr == 'S')) | ((sul == 'S') & (sur == 'M') & (sdl == 'S') & (sdr == 'M')) | ((sul == 'S') & (sur == 'S') & (sdl == 'M') & (sdr == 'M')):
        return True
    return False

def CountXMASFromOrigin(lines,i,j):
    return IsXMAS(lines,i,j,'U') + IsXMAS(lines,i,j,'UR') + IsXMAS(lines,i,j,'R') + IsXMAS(lines,i,j,'DR') + IsXMAS(lines,i,j,'D') + IsXMAS(lines,i,j,'DL') + IsXMAS(lines,i,j,'L') + IsXMAS(lines,i,j,'UL')

def CountTotalXMAS(lines):
    countXMAS = [[CountXMASFromOrigin(lines, j, i) for i in range(len(lines[0])-1)] for j in range(len(lines))]
    return sum([sum(line) for line in countXMAS])

def CountTotalX_MAS(lines):
    countX_MAS = [[IsX_MAS(lines, j, i) for i in range(len(lines[0])-1)] for j in range(len(lines))]
    return sum([sum(line) for line in countX_MAS])

lines = ReadFile("Advent4input.txt")
print(CountTotalX_MAS(lines))
from tabulate import tabulate

def ReadFile(fname):
    with open(fname, "r") as file:
        lines = [[char for char in line if not(char == '\n')] for line in file]
    return lines

def FillDictionnary(lines):
    antennas = {}
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            charAntenna = lines[i][j]
            if not(charAntenna == '.'):
                if charAntenna in antennas:
                    antennas[charAntenna].append((i,j))
                else:
                    antennas.update({charAntenna: [(i,j)]})
    return antennas

def substr(x, y):
    return (x[0] - y[0], x[1] - y[1])

def add(x,y):
    return (y[0] + x[0], y[1] + x[1])

def Includepos(i, j, antinodes):
    if not((i < 0) | (j < 0) | (i > len(antinodes)-1) | (j > (len(antinodes[0])-1))):
        antinodes[i][j] = 1

def FindCorrespondingAntinodesA(posx, posy, antinodes):
    xy = substr(posy, posx)
    pos1 = substr(posx, xy)
    Includepos(pos1[0], pos1[1], antinodes)
    pos2 = add(posy, xy)
    Includepos(pos2[0], pos2[1], antinodes)
    return antinodes

def FindCorrespondingAntinodesB(posx, posy, antinodes, almost):
    X = range(len(antinodes))

    if (posx[0] == posy[0]):
        for y in range(len(antinodes[0])):
            Includepos(posx[0], y, antinodes)

    A = float(posx[1]-posy[1]) / float(posx[0]-posy[0])
    B = posx[1] - A*posx[0]
    
    for x in X:
        y = A*x + B
        #if abs(y - int(y)) < 0.001:
        if y.is_integer():
            Includepos(x, int(y), antinodes)
            #if not(y.is_integer()):
                #print(y)
                #almost = almost+1
    return (antinodes, almost)

def GenerateAntinodes(antennas, lines, almost):
    antinodes = [[0 for col in line] for line in lines]
    for char in antennas:
        positions = antennas[char]
        for x in range(len(positions)):
            for y in range(x):
                (antinodes, almost) = FindCorrespondingAntinodesB(positions[x], positions[y], antinodes, almost)
    return (antinodes, almost)

lines = ReadFile("Advent8input.txt")
antennas = FillDictionnary(lines)
#print(antennas)
almost = 0

(antinodes, almost) = GenerateAntinodes(antennas, lines, almost)
#print(tabulate(antinodes))
print(almost)
print(sum([sum(line) for line in antinodes]))

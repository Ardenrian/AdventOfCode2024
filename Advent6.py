import copy

#  --------------> j
# |
# |
# |
# V
# i

def ReadFile(fname): #0 = nothing there, 1 = obstacle, 3 = where the guard is (2 where it has been)
    file = open(fname, "r")
    lines = [[0 if a == '.' else 1 if a == '#' else 3 for a in line if not(a== "\n")] for line in file] #0 = nothing there, 1 = obstacle, 3 = where the guard is 
    file.close()
    return lines

def NextCoord(i, j, dir):
    if dir == 'U':
        return (i-1, j)
    if dir == "D":
        return (i+1,j)
    if dir == "L":
        return (i, j-1)
    if dir == "R":
        return (i, j+1)

def NextDir(dir):
    if dir == 'U':
        return 'R'
    if dir == "D":
        return 'L'
    if dir == "L":
        return 'U'
    if dir == "R":
        return 'D'

def NextMaze(maze, i, j, dir):
    (i2, j2) = NextCoord(i, j, dir)
    if (i2<0)|(j2<0)|(i2>len(maze)-1)|(j2>len(maze[0])-1):
        maze[i][j] = 2
        return (False, maze, i, j, dir)
    if maze[i2][j2] == 1:
        return (True, maze, i, j, NextDir(dir))
    maze[i][j] = 2
    maze[i2][j2] = 3
    return (True, maze, i2, j2, dir)

def FindGuard(maze):
    for i in range(len(maze)):
        if 3 in maze[i]:
            return (i, maze[i].index(3))
    return (-1, -1)
    
def GuardWalksUntilEnd(maze): #return true if infinite
    guard = FindGuard(maze)
    cont = True
    dir = 'U'
    i = guard[0]
    j = guard[1]
    dicBeen = {(i,j,dir):True}
    while(cont):
        (cont, maze, i, j, dir) = NextMaze(maze, i, j, dir)
        if ((i,j,dir) in dicBeen) & cont:
            return (True, maze)
        dicBeen.update({(i,j,dir):True})
    return (False, maze)

def IfWeAddObstIsItInfinite(maze_, i, j):
    if not(maze_[i][j]==0):
        return False 
    newmaze = copy.deepcopy(maze_)
    newmaze[i][j] = 1
    (inf, newmaze) = GuardWalksUntilEnd(newmaze)
    print(i,j)
    return inf

maze = ReadFile("Advent6input.txt")
(temp, mazeWalked) = GuardWalksUntilEnd(copy.deepcopy(maze))
whereguardhasbeen = [[1 if x == 2 else 0 for x in line] for line in mazeWalked]
print(sum([sum(line) for line in whereguardhasbeen]))

mapInfinites = [[IfWeAddObstIsItInfinite(maze, i, j) if whereguardhasbeen[i][j]==1 else False for i in range(len(maze))] for j in range(len(maze[0]))]
print(mapInfinites)
print(sum([sum(line) for line in mapInfinites]))
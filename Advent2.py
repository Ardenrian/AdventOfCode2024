def ReadFile(fname):
    file = open(fname, "r")
    reports = [[int(val) for val in line.split()] for line in file]
    file.close()
    return reports

def IsLevelSafe(level):
    dir = level[1]-level[0] #pos inc, neg dec
    for i in range(len(level)-1):
        if (level[i+1] - level[i]) * dir <= 0:
            return 0
        if abs(level[i+1] - level[i]) > 3:
            return 0
    return 1

def IsLevelSafeWithDampener(level):
    if IsLevelSafe(level):
        return 1
    
    for i in range(len(level)):
        popped = level[:]
        popped.pop(i)
        if IsLevelSafe(popped):
            return 1

    return 0

def CountSafeLevels(reports):
    whichIsSafe = [IsLevelSafe(level) for level in reports]
    return sum(whichIsSafe)

def CountSafeLevelsWithDampener(reports):
    whichIsSafe = [IsLevelSafeWithDampener(level) for level in reports]
    return sum(whichIsSafe)

reports = ReadFile("Advent2input.txt")
print(CountSafeLevelsWithDampener(reports))

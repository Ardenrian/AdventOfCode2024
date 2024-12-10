import re
import copy

def ReadFile(fname):
    with open(fname, "r") as file:
        lines = [line for line in file]
    my_data_strings = [re.findall(r"[\d]+", line) for line in lines]
    my_data = [[int(s) for s in line] for line in my_data_strings]
    return my_data

def EvalEquation(fullEquation, operators):#0=+, 1=*, 2=||
    #take care of the 2s
    #fullEquation = copy.deepcopy(fullEquation_)
    #for i in [len(operators) - i -1 for i in range(len(operators))]:
    #    if operators[i]==2:
    #        operators[i]=0
    #        fullEquation[i+1] = int(str(fullEquation[i+1]) + str(fullEquation[i+2]))
    #        fullEquation[i+2] = 0

    #only binaries left
    result = fullEquation[1]
    for (e,o) in zip(fullEquation[2:], operators):
        if result < fullEquation[0]:
            if o == 0:
                result = result + e
            if o == 1:
                result = result * e
            if o == 2:
                result = int(str(result) + str(e))
    return result

def CreateBinaryList(number, size):
    binaryList = [int(number/pow(2,i))%2 for i in range(size)]
    return binaryList

def CreateTernaryList(number, size):
    ternaryList = [int(number/pow(3,i))%3 for i in range(size)]
    return ternaryList

def GenerateAllPossibleBinaries(size):
    binaries = [CreateBinaryList(i, size) for i in range(pow(2,size))]
    return binaries

def GenerateAllPossibleTernaries(size):
    ternaries = [CreateTernaryList(i, size) for i in range(pow(3,size))]
    return ternaries

def CanEquationBeTrueBin(fullEquation):
    binaries = GenerateAllPossibleBinaries(len(fullEquation)-2)
    for binary in binaries:
        if (EvalEquation(fullEquation, binary)) == fullEquation[0]:
            return True
    return False

def CanEquationBeTrueTer(fullEquation):
    print(fullEquation[0])
    ternaries = GenerateAllPossibleTernaries(len(fullEquation)-2)
    for ternary in ternaries:
        if (EvalEquation(fullEquation, ternary)) == fullEquation[0]:
            return True
    return False


my_data = ReadFile('Advent7input.txt')
whichCanBeTrue = [CanEquationBeTrueTer(line) for line in my_data]
print(whichCanBeTrue)
print(sum([equation[0] if canBeTrue else 0 for (canBeTrue, equation) in zip(whichCanBeTrue, my_data)]))
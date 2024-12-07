import re

def ReadFile(fname):
    file = open(fname, "r")
    lines = [line for line in file]
    file.close()
    return lines

def computeAddMuls(list):
    return sum(computeAddMul(line) for line in list)

def computeAddMul(line):
    listOfMul = re.findall("mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)", line)
    muls = [int(mul[0])*int(mul[1]) for mul in listOfMul]
    return sum(int(mul[0])*int(mul[1]) for mul in listOfMul)

def computeAddMulsWithIf(list):
    sum = 0
    count = True
    for line in list:
        listOfMul = re.findall("(?:mul\((?:\d|\d\d|\d\d\d),(?:\d|\d\d|\d\d\d)\))|(?:do\(\))|(?:don't\(\))", line)
        for item in listOfMul:
            if item == "do()":
               count = True
            elif item == "don't()":
             count = False
            elif count:
                numbers = re.findall("mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)", item)
                sum = sum + int(numbers[0][0])*int(numbers[0][1])
    return sum

list = ReadFile("Advent3input.txt")
print (computeAddMulsWithIf(list))

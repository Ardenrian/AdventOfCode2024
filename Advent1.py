def ReadFile(fname):
    file = open(fname, "r")
    my_data = [[int(val) for val in line.split()] for line in file]
    file.close()
    a = [data[0] for data in my_data]
    b = [data[1] for data in my_data]
    return a, b

def CalcDist(a, b): #1a
    a.sort()
    b.sort()
    substArray = [a1 - b1 for (a1, b1)in zip(a, b)]
    return sum (val for val in [abs(val) for val in substArray])

def CalcSimilarity(a,b): #1b
    similArray = [val if val in a else 0 for val in b]
    return sum(val for val in similArray)

a, b =  ReadFile("Advent1input.txt")
print(CalcSimilarity(a, b))

def ReadFile(fname):
    file = open(fname, "r")
    my_data = [[int(val) for val in line.split()] for line in file]
    file.close()
    a = [data[0] for data in my_data]
    b = [data[1] for data in my_data]
    return a, b

def CalcDist(a, b):
    a.sort()
    b.sort()
    subArray = [a1 - b1 for (a1, b1)in zip(a, b)]
    return sum (val for val in [abs(val) for val in subArray])

a, b =  ReadFile("Advent1input.txt")
print(CalcDist(a, b))

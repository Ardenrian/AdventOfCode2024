from tabulate import tabulate

def ReadFile(fname):
    with open(fname, "r") as file:
        lines = [[char for char in line if not(char == '\n')] for line in file]
    return lines

def ValueCrop(cropsMap, line, crop):
    if ((line<0) | (crop <0) | (line > len(cropsMap) -1) | (crop > len(cropsMap[0]) -1)):
        return -1
    return cropsMap[line][crop]

def ExploreCrop(cropsMap, countedCropsMap, line, crop, area, perimeter):
    cropsAround = []
    countedCropsMap[line][crop] = True

    if (cropsMap[line][crop] == ValueCrop(cropsMap, line-1, crop)):
        cropsAround.append((line-1, crop))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line+1, crop)):
        cropsAround.append((line+1, crop))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line, crop-1)):
        cropsAround.append((line, crop-1))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line, crop+1)):
        cropsAround.append((line, crop+1))

    area = area + 1
    perimeter = perimeter + 4 - len(cropsAround)

    for crop in cropsAround:
        if countedCropsMap[crop[0]][crop[1]] == False:
            (area, perimeter, countedCropsMap) = ExploreCrop(cropsMap, countedCropsMap, crop[0], crop[1], area, perimeter)

    return (area,perimeter, countedCropsMap)

def NumberOfCorners(cropsMap, i, j, crop):
    blocks = [(i, j), (i-1, j), (i, j-1), (i-1, j-1)]
    isTheCrop = [(ValueCrop(cropsMap, block[0], block[1]) == crop) for block in blocks]
    if ((isTheCrop[0] != isTheCrop[1]) & (isTheCrop[0] != isTheCrop[2]) & (isTheCrop[0] != isTheCrop[3])):
        return 1
    if ((isTheCrop[0] != isTheCrop[1]) & (isTheCrop[1] != isTheCrop[3]) & (isTheCrop[1] != isTheCrop[2])):
        return 1
    if ((isTheCrop[0] != isTheCrop[2]) & (isTheCrop[3] != isTheCrop[2]) & (isTheCrop[1] != isTheCrop[2])):
        return 1
    if ((isTheCrop[3] != isTheCrop[1]) & (isTheCrop[3] != isTheCrop[2]) & (isTheCrop[0] != isTheCrop[3])):
        return 1
    
    if ((isTheCrop[0] != isTheCrop[1]) & (isTheCrop[0] != isTheCrop[2]) & (isTheCrop[0] == isTheCrop[3])):
        return 2

    return 0

def FencesPrice(cropsMap):
    countedCropsMap = [[False for val in line] for line in cropsMap]
    price = 0

    for (i, line) in enumerate(cropsMap):
        for j in range(len(line)):
            if not(countedCropsMap[i][j]):
                (area, perimeter, countedCropsMap) = ExploreCrop(cropsMap, countedCropsMap, i, j, 0, 0)
                price = price + area * perimeter
    return price

def ExploreCropBulk(cropsMap, countedCropsMap, line, crop, area, numberOfCorners, listOfCorners):
    cropsAround = []
    countedCropsMap[line][crop] = True

    if (cropsMap[line][crop] == ValueCrop(cropsMap, line-1, crop)):
        cropsAround.append((line-1, crop))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line+1, crop)):
        cropsAround.append((line+1, crop))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line, crop-1)):
        cropsAround.append((line, crop-1))
    if (cropsMap[line][crop] == ValueCrop(cropsMap, line, crop+1)):
        cropsAround.append((line, crop+1))

    area = area + 1

    corners = [(a,b,NumberOfCorners(cropsMap, a, b, cropsMap[line][crop])) for a in [line, line+1] for b in [crop, crop+1]]

    #To explain the following loop with what if the corner is double. It's because of this example:
    #AAAAAA
    #AAABBA
    #AAABBA
    #ABBAAA
    #ABBAAA
    #AAAAAA
    #In this case we need the double corner with A to count double, but each of the "double corners" of B areaN,t really double corners. Nyway, we need to deal with that and that's how I did

    for corner in corners:  
        if corner[2] == 2:
            numberOfCorners += 1
            listOfCorners.append(corner)
        if corner[2] == 1:
            if not(corner in listOfCorners):
                numberOfCorners += 1
                listOfCorners.append(corner)

    for crop in cropsAround:
        if countedCropsMap[crop[0]][crop[1]] == False:
            (area, countedCropsMap, numberOfCorners, listOfCorners) = ExploreCropBulk(cropsMap, countedCropsMap, crop[0], crop[1], area, numberOfCorners, listOfCorners)

    return (area, countedCropsMap, numberOfCorners, listOfCorners)

def BulkFencesPrice(cropsMap):
    countedCropsMap = [[False for val in line] for line in cropsMap]
    price = 0
    #here we count the number of corners, instead of the perimeter. So that we don't count some several times, we'll add a list.
    for (i, line) in enumerate(cropsMap):
        for j in range(len(line)):
            if not(countedCropsMap[i][j]):
                (area, countedCropsMap, numberOfCorners, listOfCorners) = ExploreCropBulk(cropsMap, countedCropsMap, i, j, 0, 0, [])
                price = price + area * numberOfCorners
    return price

cropsMap = ReadFile("Advent12input.txt")
print(BulkFencesPrice(cropsMap))
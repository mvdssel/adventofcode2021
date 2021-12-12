from functools import reduce

def determineLowPoints(heights):
    lowPoints = list()

    for x in range(len(heights)):
        for y in range(len(heights[x])):
            if determineLowPoint(heights, x, y):
                lowPoints.append((x, y))

    return lowPoints

def determineLowPoint(heights, x, y):
    deltas = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
    xLen = len(heights)
    yLen = len(heights[x])
    isLowPoint = True
    equals = 0
    count = 0

    for xDelta, yDelta in deltas:
        xPos = x + xDelta
        yPos = y + yDelta

        if xPos >= 0 and xPos < xLen and \
           yPos >= 0 and yPos < yLen:

            count += 1

            if heights[x][y] > heights[xPos][yPos]:
                isLowPoint = False
                break

            elif heights[x][y] == heights[xPos][yPos]:
                equals += 1

    if equals == count:
        isLowPoint = False

    return isLowPoint

def determineRiskLevels(heights, points):
    pointValues = list()

    for point in points:
        pointValues.append(heights[point[0]][point[1]])
    
    return sum(pointValues) + len(pointValues)

def determineBasins(heights, lowPoints):
    basins = list()

    # Run through lowpoints
    for lowPoint in lowPoints:
        basin = determineBasin(heights, lowPoint)
        basins.append(basin)
    
    return basins

def determineBasin(heights, lowPoint):
    deltas = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
    xLen = len(heights)
    yLen = len(heights[0])

    # Create checked grid
    checked = list()
    for x in range(len(heights)):
        checked.append(list())
        for y in range(len(heights[x])):
            checked[x].append(False)
    checked[lowPoint[0]][lowPoint[1]] = True

    pointsToCheck = [lowPoint]
    basin = [pointsToCheck[-1]]

    while len(pointsToCheck) != 0:
        next = pointsToCheck.pop()
        
        for delta in deltas:
            pointToCheck = (next[0] + delta[0], next[1] + delta[1])

            if pointToCheck[0] >= 0 and \
               pointToCheck[0] < xLen and \
               pointToCheck[1] >= 0 and \
               pointToCheck[1] < yLen:

                pointToCheckHeight = heights[pointToCheck[0]][pointToCheck[1]]

                if not checked[pointToCheck[0]][pointToCheck[1]] and \
                pointToCheckHeight != 9 and \
                pointToCheckHeight > heights[next[0]][next[1]]:
                    basin.append(pointToCheck)
                    checked[pointToCheck[0]][pointToCheck[1]] = True
                    pointsToCheck.append(pointToCheck)
    
    return basin

def listLenCompare(list1, list2):
    return len(list1) - len(list2)

def findLargestBasins(basins, count):
    basins = sorted(basins, key = lambda basin: -len(basin))
    return basins[0:count]

heights = list()
# with open('09/test.txt') as f:
with open('09/input.txt') as f:
    for l in f:
        heights.append([ int(height) for height in l.strip() ])

lowPoints = determineLowPoints(heights)

print(determineRiskLevels(heights, lowPoints))

basins = determineBasins(heights, lowPoints)
largest = findLargestBasins(basins, 3)

result = reduce(lambda a, b: a * len(b), largest, 1)

print(result)
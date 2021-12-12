import math

def determineLowPoints(heights):
    lowPoints = list()

    for x in range(len(heights)):
        for y in range(len(heights[x])):
            if determineLowPoint(heights, x, y):
                lowPoints.append(heights[x][y])

    return lowPoints

def determineLowPoint(heights, x, y):
    delta = (-1, 0, 1)
    xLen = len(heights)
    isLowPoint = True

    for xDelta in delta:
        yLen = len(heights[x])
        for yDelta in delta:
            if not (xDelta == 0 and yDelta == 0):
                xPos = x + xDelta
                yPos = y + yDelta
                if xPos >= 0 and xPos < xLen and \
                   yPos >= 0 and yPos < yLen and \
                   heights[x][y] > heights[xPos][yPos]:
                    isLowPoint = False
                    break

    return isLowPoint

def determineRiskLevels(heights):
    return sum(heights) + len(heights)

heights = list()
# with open('09/test.txt') as f:
with open('09/input.txt') as f:
    for l in f:
        heights.append([ int(height) for height in l.strip() ])

lowPoints = determineLowPoints(heights)

print(lowPoints)

print(determineRiskLevels(lowPoints))

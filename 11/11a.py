from functools import reduce
from os import sync

def step(octopuses):
    hasFlashed = list()
    willFlash = list()
    xLen = len(octopuses)
    yLen = len(octopuses[0])

    # Initial energy gain
    for x in range(len(octopuses)):
        hasFlashed.append(list())

        for y in range(len(octopuses[x])):
            octopuses[x][y] += 1

            if octopuses[x][y] > 9:
                willFlash.append((x, y))
                hasFlashed[x].append(True)
            else:
                hasFlashed[x].append(False)

    # Flashing octopuses
    deltas = (-1, 0, 1)
    while len(willFlash) > 0:
        next = willFlash.pop()
        octopuses[next[0]][next[1]] = 0

        for xDelta in deltas:
            for yDelta in deltas:

                if not (xDelta == 0 and yDelta == 0):
                    adjacent = (next[0] + xDelta, next[1] + yDelta)

                    if adjacent[0] >= 0 and adjacent[0] < xLen and \
                       adjacent[1] >= 0 and adjacent[1] < yLen and \
                       not hasFlashed[adjacent[0]][adjacent[1]]:
                        octopuses[adjacent[0]][adjacent[1]] += 1

                        if octopuses[adjacent[0]][adjacent[1]] > 9:
                            willFlash.append(adjacent)
                            hasFlashed[adjacent[0]][adjacent[1]] = True
    
    return reduce(lambda acc, row: acc + sum(row), hasFlashed, 0)

def printOctopuses(octopuses):
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            print(octopuses[x][y], end='')
        print()
    print()

octopuses = list()

# with open('11/test.txt') as f:
with open('11/input.txt') as f:
# with open('11/small_test.txt') as f:
    for l in f:
        octopuses.append([ int(octopus) for octopus in l.strip() ])

flashCount = 0
syncing = False
stepCount = 0

while not syncing:
    stepCount += 1

    # print("After step %s:" % i)
    # printOctopuses(octopuses)

    newFlashes = step(octopuses)

    if newFlashes == len(octopuses) * len(octopuses[0]):
        syncing = True

    flashCount += newFlashes

print("Flashcount: %s" % flashCount)
print("Step: %s" % stepCount)
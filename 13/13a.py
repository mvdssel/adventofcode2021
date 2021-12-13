def printGrid(grid):
    lenX = len(grid)
    lenY = len(grid[0])

    for y in range(lenY):
        for x in range(lenX):
            dot = '#' if grid[x][y] else '.'
            print(dot, end='')
        print()
    print()

dots = list()
folds = list()

def foldAlongX(grid, location):
    lenX = len(grid)
    lenY = len(grid[0])

    # Redraw dots
    for x in range(location, lenX):
        for y in range(lenY):
            if grid[x][y]:
                newX = location - (x - location)
                newY = y
                grid[newX][newY] = True
                grid[x][y] = False
    
    # Resize grid
    for i in range(location):
        grid.pop()

def foldAlongY(grid, location):
    lenX = len(grid)
    lenY = len(grid[0])

    # Redraw dots
    for x in range(lenX):
        for y in range(location, lenY):
            if grid[x][y]:
                newX = x
                newY = location - (y - location)
                grid[newX][newY] = True
                grid[x][y] = False

    # Resize grid
    for x in range(lenX):
        for i in range(location):
            grid[x].pop()

def countDots(grid):
    return sum(
        [ sum(row) for row in grid ]
    )
    # count = 0

    # lenX = len(grid)
    # lenY = len(grid[0])

    # for x in range(lenX):
    #     for y in range(lenY):
    #         count += not grid[x][y]

    # return count

# Read input
isReadingFolds = False
# with open('13/test.txt') as f:
with open('13/input.txt') as f:
    for l in f:
        l = l.strip()

        if l == '':
            isReadingFolds = True
        elif isReadingFolds:
            direction, location = l.split('=')
            folds.append((direction, int(location)))
        else:
            x, y = l.split(',')
            dots.append((int(x), int(y)))

# Create grid
maxX = max([dot[0] for dot in dots])
maxY = max([dot[1] for dot in dots])
grid = list()

for x in range(maxX + 1):
    grid.append(list())
    for y in range(maxY + 1):
        grid[x].append(False)

# Add dots to grid
for dot in dots:
    grid[dot[0]][dot[1]] = True

# printGrid(grid)

for fold in folds[0:1]:
    print('%s=%s' % (fold[0], fold[1]))
        
    if fold[0] == 'fold along x':
        foldAlongX(grid, fold[1])
    else:
        foldAlongY(grid, fold[1])

    print('dot count: ', countDots(grid))
    # printGrid(grid)
    


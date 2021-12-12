def printGrid(grid):
    print("GRID")
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print("%3s" % grid[x][y], end="  ")
        
        print()
    print()

def addLine(grid, line):
    start = line[0]
    end = line[1]
    if start[0] == end[0]:
        minY = min(start[1], end[1])
        maxY = max(start[1], end[1])
        for y in range(minY, maxY + 1):
            grid[start[0]][y] += 1
    
    if start[1] == end[1]:
        minX = min(start[0], end[0])
        maxX = max(start[0], end[0])
        for x in range(minX, maxX + 1):
            grid[x][start[1]] += 1

def countCrossingPoints(grid):
    count = 0

    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] > 1:
                count += 1

    return count

# Read coords
lines = list()
maxX = 0
maxY = 0
# with open("05/test.txt") as f:
with open("05/input.txt") as f:
    for l in f:
        # Read line
        coord = l.split(" -> ")
        start = [  int(number) for number in coord[0].split(",")  ]
        end = [  int(number) for number in coord[1].split(",")  ]
        lines.append([start, end])

        # Check grid size
        maxX = max(maxX, start[0], end[0])
        maxY = max(maxX, start[1], end[1])

# Create grid
grid = list()
for x in range(maxX + 1):
    grid.append([0] * (maxY + 1))

# Draw lines
for line in lines:
    addLine(grid, line)

# printGrid(grid)
print(countCrossingPoints(grid))

# with open("07/test.txt") as f:
with open("07/input.txt") as f:
    for l in f:
        crabs = [ int(crab) for crab in l.split(",") ]

positions = list()
for i in range(max(crabs)+1):
    fuel = 0
    for crab in crabs:
        fuel += abs(crab-i)
    
    positions.append(fuel)

print(min(positions))
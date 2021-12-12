fishCount = [0] * 9

# with open("06/test.txt") as f:
with open("06/input.txt") as f:
    for l in f:
        fishes = [ int(n) for n in l.split(",") ]

for fish in fishes:
    fishCount[fish] += 1

day = 0

while day < 256:
    print("Day %2s: %s" % (day, ",".join(str(x) for x in fishCount)))

    newFishCount = fishCount[1:9]
    newFishCount.append(fishCount[0])
    newFishCount[6] += fishCount[0]

    fishCount = newFishCount
    day += 1

print(sum(fishCount))
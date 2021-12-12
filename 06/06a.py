fishes = list()

# with open("06/test.txt") as f:
with open("06/input.txt") as f:
    for l in f:
        fishes = [ int(n) for n in l.split(",") ]

day = 0

while day < 80:
    # print("Day %2s: %s" % (day, ",".join(str(x) for x in fishes)))

    newFishes = 0
    for i, fish in enumerate(fishes):
        fishes[i] -= 1

        if fishes[i] < 0:
            fishes[i] = 6
            newFishes += 1
    fishes += [8] * newFishes
    day += 1

print(len(fishes))
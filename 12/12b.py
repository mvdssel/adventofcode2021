from enum import Enum

class CaveType(Enum):
    SMALL = 1
    LARGE = 2

class Cave:
    def __init__(self, name):
        self.paths = dict()
        self.name = name
        self.caveType = CaveType.SMALL if name.islower() else CaveType.LARGE

class CavePath:
    def __init__(self):
        self.stops = list()

    def __init__(self, stops):
        self.stops = stops[:]
        self.calculateHasDoubleSmall()

    def __lt__(self, other):
        for i in range(min(len(self.stops), len(other.stops))):
            if self.stops[i].name < other.stops[i].name:
                return True
            elif self.stops[i].name > other.stops[i].name:
                return False
        
        return False

    def __str__(self):
        strRepr = ''
        for cave in self.stops:
            strRepr += cave.name + ','
        return strRepr [:-1]

    def __contains__(self, cave):
        for stop in self.stops:
            if stop.name == cave.name:
                return True
        return False

    def calculateHasDoubleSmall(self):
        caveCount = dict()
        self.hasDoubleSmall = False

        for cave in self.stops:
            caveCount[cave.name] = caveCount.get(cave.name, 0) + 1

            if caveCount[cave.name] == 2 and cave.name.islower():
                self.hasDoubleSmall = True
                break

    def canBeAdded(self, cave):
        if cave.name == 'start' or \
           cave.name == 'end' or \
           cave.caveType == CaveType.SMALL and self.hasDoubleSmall and (cave in self):
            return False

        return True

class CaveSystem:
    def __init__(self, f):
        self.caves = dict()

        for l in f:
            c1, c2 = l.strip().split('-')

            for c in (c1, c2):
                if not c in self.caves:
                    self.caves[c] = Cave(c)

            self.caves[c1].paths[c2] = self.caves[c2]
            self.caves[c2].paths[c1] = self.caves[c1]
    
    def findPaths(self, start, end):
        partialPaths = [ CavePath([ self.caves[start] ]) ]
        completePaths = list()

        while len(partialPaths) > 0:
            partialPath = partialPaths.pop()
            lastStop = partialPath.stops[-1]
            
            print(partialPath)
            for nextStopName, nextStop in lastStop.paths.items():
                newPath = CavePath(partialPath.stops[:] + [nextStop])
                if nextStopName == end:
                    # print("%s: FOUND!" % newPath)
                    completePaths.append(newPath)

                elif partialPath.canBeAdded(nextStop):
                    # print("%s: new path" % newPath)
                    partialPaths.append(newPath)
                
                # else:
                #     print("%s: not ok" % newPath)
                
            # print()
        
        return completePaths

# with open('12/test.txt') as f:
# with open('12/test_large.txt') as f:
with open('12/input.txt') as f:
    caveSystem = CaveSystem(f)

paths = caveSystem.findPaths('start', 'end')
paths.sort()

for path in paths:
    print(path)

print(len(paths))

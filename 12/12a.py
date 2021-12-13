from enum import Enum

class CaveType(Enum):
    SMALL = 1
    LARGE = 2

class Cave:
    def __init__(self, name):
        self.paths = dict()
        self.name = name
        self.caveType = CaveType.SMALL if name.islower() else CaveType.LARGE

    def canBeAddedToCavePath(self, cavePath):
        if self.caveType == CaveType.SMALL:
            for cave in cavePath:
                if self.name == cave.name:
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
        partialPaths = [ [ self.caves[start] ] ]
        completePaths = list()

        while len(partialPaths) > 0:
            partialPath = partialPaths.pop()
            lastStop = partialPath[-1]
            
            for nextStopName, nextStop in lastStop.paths.items():
                if nextStopName == end:
                    completePaths.append(partialPath[:] + [nextStop])

                elif nextStop.canBeAddedToCavePath(partialPath):
                    partialPaths.append(partialPath[:] + [nextStop])
        
        return completePaths

# with open('12/test.txt') as f:
# with open('12/test_large.txt') as f:
with open('12/input.txt') as f:
    caveSystem = CaveSystem(f)

paths = caveSystem.findPaths('start', 'end')

print(len(paths))
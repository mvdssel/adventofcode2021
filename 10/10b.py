from functools import reduce

openToClosed = {
    '(': ')',
    '[': ']',
    '{': '}', 
    '<': '>'
}
closedToOpen = { v: k for k, v in openToClosed.items() }

def isOpening(char):
    return char in openToClosed

def isClosing(char):
    return char in closedToOpen

def getMatching(char):
    if isOpening(char):
        return openToClosed.get(char)
    else:
        return closedToOpen.get(char)

closingCharactersPerLine = list()

# with open('10/test.txt') as f:
with open('10/input.txt') as f:
    for l in f:
        stack = list()
        isIllegalLine = False

        for c in l.strip():
            if isOpening(c):
                stack.append(c)
            else:
                opening = getMatching(c)
                verification = stack.pop()
                if opening != verification:
                    isIllegalLine = True
                    break

        if not isIllegalLine:
            closingCharactersPerLine.append([ getMatching(c) for c in reversed(stack)])

scoreTable = {
    ')': 1,
    ']': 2,
    '}': 3, 
    '>': 4
}

scores = list()

for closingCharacters in closingCharactersPerLine:
    scores.append(reduce(lambda acc, next: acc*5 + scoreTable.get(next), closingCharacters, 0))

score = sorted(scores)[int(len(scores) / 2)]

print(score)

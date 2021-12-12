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

illegalCharacters = list()

# with open('10/test.txt') as f:
with open('10/input.txt') as f:
    for l in f:
        stack = list()
        for c in l.strip():
            if isOpening(c):
                stack.append(c)
            else:
                opening = getMatching(c)
                verification = stack.pop()
                if opening != verification:
                    illegalCharacters.append(c)
                    break

scoreTable = {
    ')': 3,
    ']': 57,
    '}': 1197, 
    '>': 25137
}

score = reduce(lambda acc, next: acc + scoreTable.get(next), illegalCharacters, 0)

print(score)
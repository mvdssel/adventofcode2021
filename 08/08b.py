def determineNumbers(notes):
    numbers = [ set() ] * 10

    determineOne(notes, numbers)
    determineFour(notes, numbers)
    determineSeven(notes, numbers)
    determineEight(notes, numbers)
    determineNine(notes, numbers)
    determineSix(notes, numbers)
    determineZero(notes, numbers)
    determineTwo(notes, numbers)
    determineThree(notes, numbers)
    determineFive(notes, numbers)

    return numbers

def determineZero(notes, numbers): 
    for i, note in enumerate(notes):
        if len(note) == 6:
            temp = set(note)

            temp.difference_update(numbers[1])

            if len(temp) == 4:
                numbers[0] = note
                notes.pop(i)
                break

def determineOne(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 2:
            numbers[1] = note
            notes.pop(i)
            break

def determineTwo(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 5:
            temp = set(note)

            temp.difference_update(numbers[4])

            if len(temp) == 3:
                numbers[2] = note
                notes.pop(i)
                break

def determineThree(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 5:
            temp = set(note)

            temp.difference_update(numbers[2])

            if len(temp) == 1:
                numbers[3] = note
                notes.pop(i)
                break

def determineFour(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 4:
            numbers[4] = note
            notes.pop(i)
            break

def determineFive(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 5:
            temp = set(note)

            temp.difference_update(numbers[2])

            if len(temp) == 2:
                numbers[5] = note
                notes.pop(i)
                break

def determineSix(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 6:
            temp = set(note)

            temp.difference_update(numbers[1])

            if len(temp) == 5:
                numbers[6] = note
                notes.pop(i)
                break

def determineSeven(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 3:
            numbers[7] = note
            notes.pop(i)
            break
    
def determineEight(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 7:
            numbers[8] = note
            notes.pop(i)
            break

def determineNine(notes, numbers):
    for i, note in enumerate(notes):
        if len(note) == 6:
            temp = set(note)

            temp.difference_update(numbers[4])
            temp.difference_update(numbers[7])

            if len(temp) == 1:
                numbers[9] = note
                notes.pop(i)
                break

sum = 0

# with open("08/test.txt") as f:
with open("08/input.txt") as f:
    for l in f:
        notes, digits = l.split("|")
        notes = [ { letter for letter in note.strip() } for note in notes.split() ]
        digits = [ { letter for letter in digit.strip() } for digit in digits.split() ]

        numbers = determineNumbers(notes)

        tempSum = 0
        for i, digit in enumerate(digits):
            for j, number in enumerate(numbers):
                if digit == number:
                    tempSum += j * pow(10, len(digits) - i - 1)
        
        sum += tempSum

print(sum) 
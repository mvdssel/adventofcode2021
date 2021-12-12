count = 0

# with open("08/test.txt") as f:
with open("08/input.txt") as f:
    for l in f:
        notes, digits = l.split("|")
        digits = [ digit.strip() for digit in digits.split() ]
        for digit in digits:
            if len(digit) == 2 or \
               len(digit) == 3 or \
               len(digit) == 4 or \
               len(digit) == 7:
                count += 1

print(count)

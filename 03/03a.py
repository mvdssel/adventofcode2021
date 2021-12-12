#!/bin/python3

import math

bitCount = 12

sumBits = [0] * bitCount
lineCount = 0

with open("03/input.txt") as f:
    for line in f: 
        line = line.strip()
        currentBits = [ int(bit) for bit in line ]

        for i in range(bitCount):
            sumBits[i] += currentBits[i]

        lineCount += 1

gamma = 0
epsilon = 0
increment = pow(2, bitCount-1)

for i in range(bitCount):
    if sumBits[i] > lineCount/2:
        gamma += increment
    else:
        epsilon += increment
    
    increment /= 2

print("gamma:", gamma)
print("epsilon:", epsilon)
print(gamma * epsilon)
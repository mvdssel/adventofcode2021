#!/bin/python3

import math

increased = 0

previous = [ math.inf, math.inf, math.inf ]
current = [ math.inf, math.inf, math.inf ]

with open("01/input.txt") as f:
    for line in f: 
        nextNumber = int(line)

        current.insert(0, nextNumber)
        current.pop()

        currentSum = sum(current)
        previousSum = sum(previous)

        if currentSum > previousSum:
            increased += 1
        
        previous.insert(0, nextNumber)
        previous.pop()

print(increased)

#!/bin/python3

import math

increased = 0

with open("01/input.txt") as f:
    previous = math.inf
    for line in f: 
        current = int(line)

        if current > previous:
            increased += 1
        
        previous = current

print(increased)
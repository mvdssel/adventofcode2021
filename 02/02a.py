#!/bin/python3

import math

class Submarine:
    x = 0
    y = 0

    def forward(self, distance):
        self.x += distance
    
    def up(self, distance):
        self.y -= distance
    
    def down(self, distance):
        self.y += distance

sub = Submarine()

with open("02/input.txt") as f:
    for line in f: 
        command, distance = line.split()
        distance = int(distance)

        if command == "up":
            sub.up(distance)
        elif command == "down":
            sub.down(distance)
        elif command == "forward":
            sub.forward(distance
    
print(sub.x * sub.y)



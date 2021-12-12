#!/bin/python3

import math


# Inlezen van alle bits

oxygenBits = list()
CO2Bits = list()
        
with open("03/input.txt") as f:
# with open("03/test.txt") as f:
    for line in f: 
        line = line.strip()
        currentBits = [ int(bit) for bit in line ] 

        oxygenBits.append(currentBits)
        CO2Bits.append(currentBits)
        
bitCount = len(oxygenBits[0])
bitsCount = len(oxygenBits)

def isValidOxygenBit(bit, bitPosition, bitCounter, bitListLen):
    return (bitCounter >= (bitListLen / 2) and bit[bitPosition] == 1) or  \
        (bitCounter < (bitListLen / 2) and bit[bitPosition] == 0)

def isValidCO2Bit(bit, bitPosition, bitCounter, bitListLen):
    return (bitCounter >= (bitListLen / 2) and bit[bitPosition] == 0) or  \
        (bitCounter < (bitListLen / 2) and bit[bitPosition] == 1)

def binaryToDecimal(bits):
    decimal = 0
    binaryIncrement = 1

    for bit in reversed(bits):
        if bit:
            decimal += binaryIncrement
        
        binaryIncrement *= 2
    
    return decimal

def calculateBitCounter(bitsList, bitPosition):
    bitCounter = 0

    for bits in bitsList:
        bitCounter += bits[bitPosition]
    
    return bitCounter

bitPosition = 0
while len(oxygenBits) > 1:
    bitCounter = calculateBitCounter(oxygenBits, bitPosition)
    bitListLen = len(oxygenBits)
    oxygenBits[:] = [ bit for bit in oxygenBits if isValidOxygenBit(bit, bitPosition, bitCounter, bitListLen) ]

    bitPosition += 1

bitPosition = 0
while len(CO2Bits) > 1:
    bitCounter = calculateBitCounter(CO2Bits, bitPosition)
    bitListLen = len(CO2Bits)
    CO2Bits[:] = [ bit for bit in CO2Bits if isValidCO2Bit(bit, bitPosition, bitCounter, bitListLen) ]

    bitPosition += 1

oxygenRate = binaryToDecimal(oxygenBits[0])
CO2Rate = binaryToDecimal(CO2Bits[0])

print("oxygenRate:", oxygenRate)
print("CO2Rate:", CO2Rate)
print(oxygenRate * CO2Rate)

# 2572440: too low
# 3147375: too high

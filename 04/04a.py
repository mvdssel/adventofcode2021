#!/bin/python3

def printBoard(board):
    for row in board:
        for number in row:
            print("%2s" % number, end=" ")
        print()

def printBoards(board):
    for board in boards:
        printBoard(board)
        print()

class Bingo:
    round = -1

    def __init__(self, bingoNumbers, boards):
        self.bingoNumbers = bingoNumbers
        self.boards = boards
        self.winningBoards = set()

        for i, board in enumerate(self.boards):
            for j, row in enumerate(board):
                for k, number in enumerate(row):
                    boards[i][j][k] = [ number, False ]

    def play(self):
        # Start next round
        self.round += 1

        # Play a round
        bingoNumber = self.bingoNumbers[self.round]
        boardsToCheck = set()

        for i, board in enumerate(self.boards):
            for j, row in enumerate(board):
                for k, number in enumerate(row):
                    if number[0] == bingoNumber:
                        boards[i][j][k][1] = True
                        boardsToCheck.add(i)
        
        # Print round
        print("Round %2s" % self.round)
        print("========")
        self.printBoards(self.boards)
        print()
        
        # Check for winning boards
        self.winningBoards = self.checkWinningBoards(boardsToCheck)

    def hasWinningBoard(self):
        return len(self.winningBoards) > 0
    
    def getWinningBoards(self):
        return self.winningBoards

    def checkWinningBoards(self, boardIndices):
        winningBoards = set()

        for boardIndex in boardIndices:
            if self.isWinningBoard(boardIndex):
                winningBoards.add(boardIndex)
        
        return winningBoards
    
    def isWinningBoard(self, boardIndex):
        board = self.boards[boardIndex]

        for i in range(len(board)):
            row = ( board[i][j] for j in range(len(board[i])) )
            if self.isWinningList(row):
                return True

            col = ( board[j][i] for j in range(len(board[i])) )
            if self.isWinningList(col):
                return True

        return False
    
    def isWinningList(self, list):
        isWinning = True

        for number in list:
            isWinning = isWinning and number[1]

        return isWinning

    def printBoard(self, board):
        for row in board:
            for number in row:
                mark = "X" if number[1] else " "
                print("[%s] %2s" % (mark, number[0]), end="   ")
            print()

    def printBoards(self, boards):
        for board in boards:
            self.printBoard(board)
            print()

    def printBoardIndices(self, boardIndices):
        for boardIndex in boardIndices:
            self.printBoard(self.boards[boardIndex])
            print()

    def calculateWinningBoardScore(self, board):
        score = 0

        for row in board:
            for number in row:
                if not number[1]:
                    score += number[0]

        score *= self.bingoNumbers[self.round]
        return score



# with open("04/test.txt") as f: 
with open("04/input.txt") as f: 
    bingoNumbers = [ int(number) for number in next(f).split(",") ]
    next(f)

    boards = list()
    currentBoard = list()
    
    for line in f:
        boardNumbers = [ int(number) for number in line.split() ]
        if len(boardNumbers) == 0:
            boards.append(currentBoard)
            currentBoard = list()
        else:
            currentBoard.append(boardNumbers)
    
    boards.append(currentBoard)

bingo = Bingo(bingoNumbers, boards)
bingo.printBoards(bingo.boards)

while not bingo.hasWinningBoard():
    bingo.play()


winningBoards = bingo.getWinningBoards()
print("Winning boards")
print("==============")
for index in winningBoards:
    board = bingo.boards[index]
    score = bingo.calculateWinningBoardScore(board)
    print("Score: ", score)
    bingo.printBoard(board)
    print()

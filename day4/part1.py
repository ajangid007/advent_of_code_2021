import os
import sys

boards = []
draws = []

def readInput(inputfile):
    global boards
    global draws
    board = []
    lines = open(os.path.join(sys.path[0], inputfile), "r")
    for line in lines:
        if len(draws) == 0:
            draws = [int(x) for x in line.split(",")]
            continue
        if line == "\n":
            if board:
                boards.append(board)
                board = []
            continue
        else:
            board.append([int(x) for x in line.split()])
    return

def findWinningBoard():
    global draws
    winningBoardIndex = 0
    for draw in draws:
        updateBoards(draw)
        winningBoardIndex = evaluateBoards()

        if winningBoardIndex:
            return sumBoard(winningBoardIndex[0]) * draw
        
def sumBoard(index):
    global boards
    return sum(sum(boards[index], []))

def updateBoards(draw):
    global boards
    for i in range(len(boards)):
        boards[i] = [[0 if _el == draw else _el for _el in row] for row in boards[i]]
    return 
        
def evaluateBoards():
    global boards
    winningBoardIndex = []
    for i in range(len(boards)):
        if winningRows(boards[i]) or winningColumns(boards[i]):
            winningBoardIndex.append(i)
    return winningBoardIndex

def winningRows(board):
    rows = [True] * len(board)
    for i in range(len(board)):
        for element in board[i]:
            if element != 0:
                rows[i] = False
                break
    return any(rows)

def winningColumns(board):
    columns = [True] * len(board[0])
    for i in range(len(board[0])):
        for element in [row[i] for row in board]:
            if element != 0:
                columns[i] = False
                break
    return any(columns)

if __name__ == '__main__':
    #https://adventofcode.com/2021/day/4
    readInput('input.txt')
    winnningValue = findWinningBoard()
    print(winnningValue)

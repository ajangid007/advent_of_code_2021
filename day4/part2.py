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

def findWinningBoardLast():
    global boards
    global draws
    winningBoardIndex = []
    for i in range(len(boards)):
        (drawindex, boards[i]) = evaluateBoard(boards[i])
        if drawindex:
            winningBoardIndex.append(drawindex)
    max = 0
    for drawCount in winningBoardIndex:
        if drawCount > max:
            max = drawCount
    print("board index = " + str(winningBoardIndex.index(max)) + ", board = " + str(boards[winningBoardIndex.index(max)]))
    print("draw count = " + str(max) + ", draw value = " + str(draws[max-1]))
    print(sumBoard(winningBoardIndex.index(max)) * (draws[max-1]))
        
def sumBoard(index):
    global boards
    return sum([sum(x) for x in boards[index]])

def updateBoard(board, draw):
    for i in range(len(board)):
        board = [[0 if _el == draw else _el for _el in row] for row in board]
    return board
        
def evaluateBoard(board):
    global draws
    index = 0
    for draw in draws:
        index += 1
        board = updateBoard(board, draw)
        if winningRows(board) or winningColumns(board):
            return (index, board)
    return (None, board)

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
    findWinningBoardLast()

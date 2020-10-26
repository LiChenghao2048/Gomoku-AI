from Rules import *
from Strategy import *

def multiPlayers(boardSize):
    board = newGame(boardSize)
    while True:
        board = newTurn(board)
        if checkEnd(board):
            break


def singlePlayer(boardSize, alogrithm):
    board = newGame(boardSize)
    #board = firstMove(board)
    while True:
        board = blackTurn(board)
        if checkEnd(board):
            break
        if alogrithm == 0:
            board = zero(board, "O")
        elif alogrithm == 1:
            board = minimaxLv2(board, "O")
        elif alogrithm == 2:
            board = minimaxLv3(board, "O")
        elif alogrithm == 3:
            board = minimaxLv4(board, "O")
        if checkEnd(board):
            break

def battleAI(boardSize, alogrithm1, alogrithm2):
    board = newGame(boardSize)
    board = firstMove(board)
    numRound = 0
    while True:
        try:
            print("ROUND", numRound)

            print("White Turn:")
            if alogrithm2 == 0:
                board = zero(board, "O")
            elif alogrithm2 == 1:
                board = minimaxLv2(board, "O")
            elif alogrithm2 == 2:
                board = minimaxLv3(board, "O")
            elif alogrithm2 == 3:
                board = minimaxLv4(board, "O")
            if checkEnd(board):
                return ["O", numRound]

            print("Black Turn:")
            if alogrithm1 == 0:
                board = zero(board, "X")
            elif alogrithm1 == 1:
                board = minimaxLv2(board, "X")
            elif alogrithm1 == 2:
                board = minimaxLv3(board, "X")
            elif alogrithm2 == 3:
                board = minimaxLv4(board, "X")
            if checkEnd(board):
                return ["X", numRound]

            numRound += 1

        except:
            return ["T", numRound]
    

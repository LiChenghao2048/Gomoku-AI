import random

def newGame(boardSize):
    board = []
    for i in range(boardSize + 1):
        row = []
        for j in range(boardSize):
            if j == 0:
                row.append(str(i%10))        
            row.append(" ")
        board.append(row)
    for n in range(boardSize + 1):
        board[0][n] = str(n%10)
    showGame(board)
    return board

def showGame(board):
    for i in board:
        print(i)
    return

def newTurn(board):
    blackStone = list(map(int, input("Place the Black Stone: ").split(" ")))
    board = blackTurn(board, blackStone)
    if board == "Black Win!":
        return board
    whiteStone = list(map(int, input("Place the White Stone: ").split(" ")))
    board = whiteTurn(board, whiteStone)
    return board

def blackTurn(board, blackStone = []):
    if blackStone == []:
        while True:
            try:        
                blackStone = list(map(int, input("Place the Black Stone: ").split(" ")))
                row, col = blackStone
                if board[row][col] == " ":
                    break
                print("Invalid Move.")            
            except:
                print("Invalid Move.") 
                continue 
    board = placing(blackStone, board, color = "X")
    showGame(board)
    if checkWin(blackStone, board, color = "X"):
        return "Black Win!"
    return board

def whiteTurn(board, whiteStone = []):
    if whiteStone == []:
        while True:
            try:        
                whiteStone = list(map(int, input("Place the White Stone: ").split(" ")))
                row, col = whiteStone
                if board[row][col] == " ":
                    break
                print("Invalid Move.")            
            except:
                print("Invalid Move.") 
                continue 
    board = placing(whiteStone, board, color = "O")
    showGame(board)
    if checkWin(whiteStone, board, color = "O"):
        return "White Win!"
    return board

def placing(stone, board, color):
    row, col = stone
    board[row][col] = color
    return board


def checkWin(prevMove, board, color, stoneRequire = 5):
    # Change the Stone Requirement Up Here!
    horiCheck = horiCount(prevMove, board, color, stoneRequire) 
    vertiCheck = vertiCount(prevMove, board, color, stoneRequire) 
    diagCheck1 = diagCount1(prevMove, board, color, stoneRequire) 
    diagCheck2 = diagCount2(prevMove, board, color, stoneRequire)   
    return horiCheck or vertiCheck or diagCheck1 or diagCheck2

def horiCount(prevMove, board, color, stoneRequire):
    row, col = prevMove
    length = 1
    n = 1
    m = 1
    while board[row][col - n] == color:
        length += 1
        n += 1
    while (col + m < len(board)) and (board[row][col + m] == color):
        length += 1
        m += 1
    if length >= stoneRequire:
        return True
    else:
        return False

def vertiCount(prevMove, board, color, stoneRequire):
    row, col = prevMove
    length = 1
    n = 1
    m = 1
    while board[row - n][col] == color:
        length += 1
        n += 1
    while (row + m < len(board)) and (board[row + m][col] == color):
        length += 1
        m += 1
    if length >= stoneRequire:
        return True
    else:
        return False

def diagCount1(prevMove, board, color, stoneRequire):
    row, col = prevMove
    length = 1
    n = 1
    m = 1
    while board[row - n][col - n] == color:
        length += 1
        n += 1
    while (row + m < len(board)) and (col + m < len(board)) and (board[row + m][col + m] == color):
        length += 1
        m += 1
    if length >= stoneRequire:
        return True
    else:
        return False

def diagCount2(prevMove, board, color, stoneRequire):
    row, col = prevMove
    length = 1
    n = 1
    m = 1
    while (row + n < len(board)) and (board[row + n][col - n] == color):
        length += 1
        n += 1
    while (col + m < len(board)) and (board[row - m][col + m] == color):
        length += 1
        m += 1
    if length >= stoneRequire:
        return True
    else:
        return False

def checkEnd(board):
    if board == "Black Win!" or board == "White Win!":
        print(board)
        return True
    return False
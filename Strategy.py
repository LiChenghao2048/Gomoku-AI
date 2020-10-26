import random
from Rules import *

def possibleNextMove(board):
    result = firstPeak(board)
    #result = secondPeak(board, result)
    return result

def firstPeak(board):
    result = []
    for i in range(1, len(board)):
        for j in range(1, len(board)):
            if board[i][j] == " ":
                peripheral = getPeripheral(i, j, board)
                if ("X" in peripheral) or ("O" in peripheral):
                    result.append([i, j])
    return result

def secondPeak(board, firstPeak):
    tempBoard = []
    for i in board:
        tempRow = []
        for j in i:
            tempRow.append(j)
        tempBoard.append(tempRow)    
    result = []
    for z in firstPeak:
        result.append(z)
        tempBoard[z[0]][z[1]] = "P"
    for m in range(1, len(tempBoard)):
        for n in range(1, len(tempBoard)):
            if tempBoard[m][n] == " ":
                peripheral = getPeripheral(m, n, tempBoard)
                if ("X" in peripheral) or ("O" in peripheral) or ("P" in peripheral):
                    result.append([m, n])    
    return result

def getPeripheral(row, col, board):
    """get the status of surrounding slots of the input position"""
    peripheral = ["/", "/", "/", "/", "/", "/", "/", "/"]
    if (row == 1) or (row == len(board) - 1) or (col == 1) or (col == len(board) - 1):
        # Object in the corner
        if (row == 1) and (col == 1):
            peripheral[4] = board[row][col + 1]
            peripheral[6] = board[row + 1][col]
            peripheral[7] = board[row + 1][col + 1]
            return peripheral
        if (row == 1) and (col == len(board) - 1):
            peripheral[3] = board[row][col - 1]
            peripheral[5] = board[row + 1][col - 1]
            peripheral[6] = board[row + 1][col]
            return peripheral
        if (row == len(board) - 1) and (col == 1):
            peripheral[1] = board[row - 1][col]
            peripheral[2] = board[row - 1][col + 1]
            peripheral[4] = board[row][col + 1]
            return peripheral
        if (row == len(board) - 1) and (col == len(board) - 1):
            peripheral[0] = board[row - 1][col - 1]
            peripheral[1] = board[row - 1][col]
            peripheral[3] = board[row][col - 1]
            return peripheral
        # Object at the edge
        if row == 1: 
            peripheral[3] = board[row][col - 1]
            peripheral[4] = board[row][col + 1]
            peripheral[5] = board[row + 1][col - 1]
            peripheral[6] = board[row + 1][col]
            peripheral[7] = board[row + 1][col + 1]
            return peripheral
        if row == len(board) - 1:
            peripheral[0] = board[row - 1][col - 1]
            peripheral[1] = board[row - 1][col]
            peripheral[2] = board[row - 1][col + 1]
            peripheral[3] = board[row][col - 1]
            peripheral[4] = board[row][col + 1]
            return peripheral
        if col == 1:
            peripheral[1] = board[row - 1][col]
            peripheral[2] = board[row - 1][col + 1]
            peripheral[4] = board[row][col + 1]
            peripheral[6] = board[row + 1][col]
            peripheral[7] = board[row + 1][col + 1]
            return peripheral
        if col == len(board) - 1:
            peripheral[0] = board[row - 1][col - 1]
            peripheral[1] = board[row - 1][col]
            peripheral[3] = board[row][col - 1]
            peripheral[5] = board[row + 1][col - 1]
            peripheral[6] = board[row + 1][col]
            return peripheral
    else:
        # Object in the middle
        peripheral[0] = board[row - 1][col - 1]
        peripheral[1] = board[row - 1][col]
        peripheral[2] = board[row - 1][col + 1]
        peripheral[3] = board[row][col - 1]
        peripheral[4] = board[row][col + 1]
        peripheral[5] = board[row + 1][col - 1]
        peripheral[6] = board[row + 1][col]
        peripheral[7] = board[row + 1][col + 1]
        return peripheral

def minimaxLv0(board, color):
    moves = firstPeak(board)
    move = random.choice(moves)
    print(move)
    if color == "O":
        board = whiteTurn(board, move)
    else:
        board = blackTurn(board, move)
    return board

def firstMove(board):
    print("Black Turn:")
    row = len(board) // 2
    col = row
    print([row, col])
    board = placing([row, col], board, "X")
    showGame(board)
    return board

def creatTempBoard(board, move, color):
    # copy and paste the gameboard
    tempBoard = []
    for i in board:
        tempRow = []
        for j in i:
            tempRow.append(j)
        tempBoard.append(tempRow)
    # set each possible next move as the next move
    tempBoard[move[0]][move[1]] = color

    return tempBoard

def getOppo(color):
    if color == "X":
        return "O"
    else: 
        return "X"
    

# The following functions calculates the score difference between two colors. IMPORTANT! ESSENTIAL!!
def gameEvaluate(board):
    """Base on the board, calculate the score for both colors, then return the difference"""
    blackAnalysis = baordAnalysis(board, "X")
    blackScore = getScore(blackAnalysis)
    whiteAnalysis = baordAnalysis(board, "O")
    whiteScore = getScore(whiteAnalysis)
    delta = blackScore - whiteScore
    return delta

def baordAnalysis(board, color):
    """return a list of three list: lines of stones without blocking, lines of stones with one blocking, lines of stones with two blocking"""
    result = []
    noBlocking = []
    oneBlocking = []
    twoBlocking = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == color:
                surrounding = getPeripheral(i, j, board)
                for m in range(4, 8):
                    if surrounding[m] == color and surrounding[7 - m] != color:
                        line, numBlocking = lineAnalysis(i, j, m, board, surrounding[7 - m])
                        if numBlocking == 0:
                            noBlocking.append(line)
                        elif numBlocking == 1:
                            oneBlocking.append(line)
                        else:
                            twoBlocking.append(line)
    result.append(noBlocking)
    result.append(oneBlocking)
    result.append(twoBlocking)
    return result

def lineAnalysis(row, col, idx, board, endStatus1):
    """based a given point and direction, return the entire line and the number of blockings"""
    restult = []

    line = []
    line.append([row, col])

    if endStatus1 == " ":
        numBlocking = 0
    else: 
        numBlocking = 1

    if idx == 4:
        rowChange = 0
        colChange = 1
    elif idx == 5:
        rowChange = 1
        colChange = -1
    elif idx == 6:
        rowChange = 1
        colChange = 0
    elif idx == 7:
        rowChange = 1
        colChange = 1

    color = board[row][col]

    while True:
        row += rowChange
        col += colChange
        if row == len(board) or col == len(board):
            endStatus2 = "/"
            break
        elif board[row][col] == color:
            line.append([row, col])
        else: 
            endStatus2 = board[row][col]
            break

    if endStatus2 != " ":
        numBlocking += 1

    restult.append(line)
    restult.append(numBlocking)

    return restult

def getScore(colorAnalysis):
    zeroBlockinglen = [0]
    oneBlockinglen = [0]
    twoBlockinglen = [0]

    for line in colorAnalysis[0]:
        length = len(line)
        zeroBlockinglen.append(length)
    for line in colorAnalysis[1]:
        length = len(line)
        oneBlockinglen.append(length)
    for line in colorAnalysis[2]:
        length = len(line)
        twoBlockinglen.append(length)

    a = max(zeroBlockinglen)
    b = max(oneBlockinglen) - 1
    c = max(twoBlockinglen) - 2

    
    #num_a = 0
    #for i in zeroBlockinglen:
    #    if i == a:
    #        num_a += 1
    #if num_a >= 2:
    #    a += 1

    score = 2 ** max(a, b)

    #if max(zeroBlockinglen) >= 5 or max(oneBlockinglen) >= 5 or max(twoBlockinglen) >= 5:
    #    score = score ** (max(max(zeroBlockinglen), max(oneBlockinglen), max(twoBlockinglen)) - 3)
        
    return score

# The follwing functions treverse through all possible next moves, then return the option with the highest score

def optimizeReult(scores, moves, color):
    results = []
    if color == "X":
        score = max(scores)
        for n in range(len(scores)):
            if scores[n] == score:
                results.append(moves[n])
    elif color == "O":
        score = min(scores)
        for m in range(len(scores)):
            if scores[m] == score:
                results.append(moves[m])

    return [results, score]

def minimaxLv4(board, color):
    moves = possibleNextMove(board)
    [lv2results, _] = lv2(board, color, moves)
    print((len(lv2results)), " Option(s):", lv2results)

    if len(lv2results) == 1:
        result = lv2results[0]
    else:
        print("Evaluating...")
        [lv3Results, _] = lv3(board, color, lv2results)
        print(str(len(lv3Results)), " Option(s):", lv3Results)
        if len(lv3Results) == 1:
            result = lv3Results[0]
        elif len(lv3Results) <= 3:
            print("Further Evaluating...")
            [lv4Results, _] = lv4(board, color, lv3Results)
            print(str(len(lv4Results)), " Option(s):", lv4Results)
            result = random.choice(lv4Results)
        else:
            result = random.choice(lv3Results)

    print(result)
    if color == "O":
        board = whiteTurn(board, result)
    else:
        board = blackTurn(board, result)
    
    return board


def lv4(board, color, moves):
    oppoColor = getOppo(color)

    decentMoves = []
    scores = []
    for move in moves:
        tempBoard = creatTempBoard(board, move, color)
        newMoves = possibleNextMove(tempBoard)
        [_, bestScore] = lv3(tempBoard, oppoColor, newMoves)
        if bestScore == None:
            continue
        decentMoves.append(move)
        scores.append(bestScore)

    if decentMoves == []:
        print("Good Job")
        return [[moves[0]], None]

    [newMoves, newScore] = optimizeReult(scores, decentMoves, color)
    return [newMoves, newScore]

'''
def ult(board, color, move):
    oppoColor = getOppo(color)
    tempBoard_1 = creatTempBoard(board, move, color)
    if checkWin(move, tempBoard_1, color):
        #print("case 1")
        return True
    else:
        #print("case 2")
        nextMoves = possibleNextMove(tempBoard_1)
        bol1 = False
        for nextMove in nextMoves:
            tempBoard_2 = []
            tempBoard_2 = creatTempBoard(tempBoard_1, nextMove, oppoColor)
            bol1 = bol1 or checkWin(nextMove, tempBoard_2, oppoColor)
            if bol1:
                return False
        for nextMove in nextMoves:
            tempBoard_2 = []
            tempBoard_2 = creatTempBoard(tempBoard_1, nextMove, oppoColor)
            bol2 = False
            for thirdMove in possibleNextMove(tempBoard_2):
                bol2 = bol2 or ult(tempBoard_2, color, thirdMove)
                if bol2 == 1:
                    return True
            return False

def ulti(board, color, counter = 2):
    if counter == 0:
        return [False]    
    oppoColor = getOppo(color)
    results = []
    for move_1 in possibleNextMove(board):
        tempBoard_1 = creatTempBoard(board, move_1, color)
        if checkWin(move_1, tempBoard_1, color):
            results.append(True)
            continue
        else:
            lose = [False]
            for move_2 in possibleNextMove(tempBoard_1):
                tempBoard_2 = creatTempBoard(tempBoard_1, move_2, oppoColor)
                lose.append(checkWin(move_2, tempBoard_2, oppoColor))
            if any(lose):
                results.append(False)
                continue
            for move_2 in possibleNextMove(tempBoard_1):
                tempBoard_2 = creatTempBoard(tempBoard_1, move_2, oppoColor)
                results.append(any(ulti(tempBoard_2, color, counter - 1)))
                continue
    return results

def minimaxLv4(board, color):
    moves = possibleNextMove(board)
    if any(ulti(board, color)):
        move = moves[ulti.index(True)]
    else:
        print("I surrender")
        move = moves[0]

    print(move)
    if color == "O":
        board = whiteTurn(board, move)
    else:
        board = blackTurn(board, move)
    
    return board
'''


def minimaxLv3(board, color):
    moves = possibleNextMove(board)
    [results, _] = lv2(board, color, moves)
    print(str(len(results)), " Option(s):", results)

    if len(results) == 1:
        result = results[0]
    else:
        print("Further Evaluating...")
        [newResult, _] = lv3(board, color, results)
        print(str(len(newResult)), " Option(s):", newResult)
        result = random.choice(newResult)

    print(result)
    if color == "O":
        board = whiteTurn(board, result)
    else:
        board = blackTurn(board, result)
    
    return board

def lv3(board, color, moves):
    oppoColor = getOppo(color)

    scores = []
    for move in moves:
        tempBoard = creatTempBoard(board, move, color)
        newMoves = possibleNextMove(tempBoard)
        [_, bestScore] = lv2(tempBoard, oppoColor, newMoves)
        if bestScore == None:
            return [[move], bestScore]
        else:
            scores.append(bestScore)

    [newMoves, newScore] = optimizeReult(scores, moves, color)
    return [newMoves, newScore]

def minimaxLv2(board, color):
    moves = possibleNextMove(board)

    [results, _] = lv2(board, color, moves)
    result = random.choice(results)
    
    print(result)
    if color == "O":
        board = whiteTurn(board, result)
    else:
        board = blackTurn(board, result)

    return board


def lv2(board, color, moves):
    oppoColor = getOppo(color)

    decentMoves = []
    scores = []
    for move in moves:
        # copy and paste the gameboard
        tempBoard = creatTempBoard(board, move, color)

        if checkWin(move, tempBoard, color):
            return [[move], None]

        # get the best next move for the other color after the current move
        tempBoard = lv1(tempBoard, oppoColor)
        if tempBoard == "":
            continue
        score = gameEvaluate(tempBoard)
        scores.append(score)
        decentMoves.append(move)

    if scores == []:
        print("Good Game")
        return [[moves[0]], None]

    [results, bestScore] = optimizeReult(scores, decentMoves, color)
    return [results, bestScore]


def lv1(board, color):
    # get all possible next moves
    moves = possibleNextMove(board)
    scores = []
    for move in moves:
        tempBoard = creatTempBoard(board, move, color)

        if checkWin(move, tempBoard, color):
            return ""

        # evaluate the game after this move
        score = gameEvaluate(tempBoard)
        # record the game evaluation
        scores.append(score)

    # for all evaluations, find the move with best score for the input color
    [results, _] = optimizeReult(scores, moves, color)
    result = random.choice(results)
    board[result[0]][result[1]] = color

    return board

# The following codes is trying to combine multiple algorithms into a better one.
def zero(board, color):
    moves = possibleNextMove(board)
    [results, _] = lv2(board, color, moves)
    print(str(len(results)), " Option(s):", results)

    if len(results) == 1:
        result = results[0]
    else:
        print("Further Evaluating...")
        [newResults, _] = lv3(board, color, results)
        print(str(len(newResults)), " Option(s):", newResults)
        if len(newResults) < len(results):
            result = random.choice(newResults)
        else:
            print("Evaluate from the opponent's pespective:")
            oppoResults = rezero(board, color)
            print("Opponent is likely to have", len(oppoResults), "option(s):", oppoResults)
            commonResults = []
            for a in oppoResults:
                if a in newResults:
                    commonResults.append(a)
            if commonResults:
                print(len(commonResults), "Options in Common:", commonResults)
                result = random.choice(commonResults)
            else:
                print("No common options.")
                if len(newResults) < len(oppoResults):
                    result = random.choice(newResults)
                else:
                    result = random.choice(oppoResults)
    
    print(result)
    if color == "O":
        board = whiteTurn(board, result)
    else:
        board = blackTurn(board, result)

    return board

def rezero(board, color):
    oppoColor = getOppo(color)
    moves = possibleNextMove(board)
    [results, _] = lv2(board, oppoColor, moves)
    print("LV2 Options:", results)
    if len(results) == 1:
        return results
    else:
        [newResults, _] = lv3(board, oppoColor, results)
        print("LV3 Options:", newResults)
        return newResults
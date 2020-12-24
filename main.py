#board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
#Player going
letter = "X"


def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[3])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])



def playGame():

    # Showing the initial Board
    displayBoard()

    while gameGoing:
        handleTurn()
        checkGoing()
        switchLetter()


def checkGoing():
    checkWin()
    checkTie()

def checkWin():
    #check 3 rows
    #check 3 columns
    #check 2 diagonals
    return

def checkTie():
    #if not win and board full -> there is a tie
    return

def switchLetter():
    if(letter is "X"):
        letter = "O"
    else:
        letter = "X"

def handleTurn():
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = letter
    displayBoard()



##Main
playGame()



#display Board


#playing Game
#handle turn



#isThere a win
    #check rows
    #check columns
    #check diagonals

#cat Game (entire board full + no winner)


#handle turns
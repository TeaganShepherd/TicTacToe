#------------Global Variables--------------

#board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
#Player going
letter = "X"

#Is game still playable?
gameGoing = True

#The winner
winner = None
#-----------End Global Variables-----------

def displayBoard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])



def playGame():
    global gameGoing

    # Showing the initial Board
    displayBoard()

    while gameGoing:
        handleTurn()
        checkGoing()
        switchLetter()
    
    #Game ends once we break the loop
    if (winner == None):
        print ("There was no winner. Tie game")
    else:
        print ("The winner was: " + winner)


def checkGoing():
    global gameGoing
    checkWin()
    if(gameGoing):
        checkTie()

def checkWin():
    global gameGoing
    global winner
    #check 3 rows
    #X win
    if( (board[0] == board[1] == board[2] == "X") or (board[3] == board[4] == board[5]  == "X") or (board[6] == board[7] == board[8]  == "X")  ):
        winner = "X"
        gameGoing = False
    #O win
    if( (board[0] == board[1] == board[2] == "O") or (board[3] == board[4] == board[5]  == "O") or (board[6] == board[7] == board[8]  == "O")  ):
        winner = "O"
        gameGoing = False
    
    #check 3 columns
     #X win
    if( (board[0] == board[3] == board[6] == "X") or (board[1] == board[4] == board[7]  == "X") or (board[2] == board[5] == board[8]  == "X")  ):
        winner = "X"
        gameGoing = False
    #O win
    if( (board[0] == board[3] == board[6] == "O") or (board[1] == board[4] == board[7]  == "O") or (board[2] == board[5] == board[8]  == "O")  ):
        winner = "O"
        gameGoing = False

    #check 2 diagonals
     #X win
    if( (board[0] == board[4] == board[8] == "X") or (board[2] == board[4] == board[6]  == "X")  ):
        winner = "X"
        gameGoing = False
    #O win
    if( (board[0] == board[4] == board[8] == "O") or (board[2] == board[4] == board[6]  == "O") ):
        winner = "O"
        gameGoing = False
    if(gameGoing is False):
        return True
    return False

def checkTie():
    global gameGoing
    #if not win and board full -> there is a tie
    full = True
    for mark in board:
        isMarked = not(mark is "X" or mark is "O")
        if(isMarked):
            full = False
    gameGoing = (checkWin() or not full)

def switchLetter():
    global letter
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
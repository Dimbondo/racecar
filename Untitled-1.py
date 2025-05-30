import os #used to clear the screen
os.system('cls') #clears the screen at the start

input("Welcome to Tic Tac Toe! Press enter to start") #welcome message
pInput=input("press p for player vs player, or c for computer vs player") #game mode selection
#variables for the game
X="\033[31mX\033[0m"
O="\033[34mO\033[0m" 
turn=1
board=[1,2,3,4,5,6,7,8,9] 
def clr(): #function to clear the screen
    os.system('cls')
def invalidMessage(): #function to print invalid input message
    clr()
    print("Invalid input")
    input("Press enter to continue")
def checkDraw(): #counts the amount of empty spaces, if there are none and no player wins, it is a draw
    count=0
    for i in range(9):
        if board[i]!=X and board[i]!=O:
            count+=1
    if count==0:
        clr()
        print("Draw!")
        input("Press enter to exit")
        raise SystemExit   
def checkWin(player): #checks if a player has won by checking all possible winning combinations
    count=0
    for i in range(3):
        if(board[count]==player and board[count+1]==player and board[count+2]==player): #horizontal
            return True
        count+=3
    count=0
    for i in range(3):
        if(board[count]==player and board[count+3]==player and board[count+6]==player):#vertical
            return True
        count+=1
    if(board[0]==player and board[4]==player and board[8]==player):#diagonals
        return True
    if(board[2]==player and board[4]==player and board[6]==player):
        return True   
def updBoard(): #clears the board and prints the board based on the list
    clr()
    global board
    print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    print("--+---+--")
    print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    print("--+---+--")
    print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))

 #first board print
def pvp ():
    global turn, board
    updBoard()
    checkDraw()
    print("player" + str(turn)+"'s turn") #prints whose turn it is
    move=input("Enter a number from 1 to 9: ")
    if move=="" or move.isdigit()==False: #checks if the move is empty or not a number
        invalidMessage()
        updBoard()
        pvp()
    #it converts it to an int to be used
    move=int(move)
    if move>9 or move<1: #if the move is out of range, it is invalid
        os.system('cls')
        invalidMessage()
        updBoard()
        pvp()
    if board[move-1]!=X and board[move-1]!=O: #checks if the space is empty
        if turn==1: #checks whose turn it is
            board[move-1]=X #changes the board and then changes the turn
            turn=2
            if checkWin(X): #checks if the player has won, if they have, it clears the screen and prints the winner
                clr()
                print("Player 1 wins!")
                input("Press enter to exit")
                raise SystemExit     #exits the game as there is no more code to run
            pvp() #calls the function again to continue the game
        else: #same thing as above, but for player 2
            board[move-1]=O
            turn=1
            if checkWin(O):
                clr()
                print("Player 2 wins!")
                input("Press enter to exit")
                raise SystemExit
            pvp()
    else: #if the space is already taken, it is invalid
        clr()
        invalidMessage()
    updBoard()
#_____________________________________________________________________________________________________________________
#cvp functions and game

def cvp():
    print("Computer vs player mode is not implemented yet")
    input("Press enter to exit")
    raise SystemExit
while True: #infinite loop to keep the game running until a gamemode is selected
    if (pInput=="p"):
        pvp() #if the input is not p, it will exit the game
        break
    elif(pInput=="c"):
        cvp()
        break
    else:
        print("press enter to try again")
        continue


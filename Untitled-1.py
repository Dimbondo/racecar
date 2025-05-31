import os #used to clear the screen
import random #used for the computer to make random moves
os.system('cls') #clears the screen at the start


#variables for the game
X="\033[31mX\033[0m"
O="\033[34mO\033[0m" 
Pmove=1
turn=1
board=[1,2,3,4,5,6,7,8,9] 
Win=True
Lose=False

#all functions for pvp
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
        cvp()
    updBoard()
#_____________________________________________________________________________________________________________________
#cvp functions and game
def canwin(i): #checks if the player can win in the next move
    global board, turn
    for j in range(9):
        if board[j]!=O and board[j]!=X:
            board[j]=i
            if (checkWin(i)):
                if i==X:
                   turn=2 #if the player can win, it changes the turn to the computer
                board[j]=O
                return
            board[j]=j+1 #if the player cannot win, it resets the space
                


    
def middle():
    global board
    if board[4]==X or board[4]==O: #if the middle space is taken, it returns false
        ()
    else:
        board[4]=O #if it is empty, it takes it
def cvp():
    global turn, board, Win, Lose, Pmove
    updBoard()
    checkDraw()

    if(turn==1):
        print("player 1's turn") #prints whose turn it is
        Pmove=input("Enter a number from 1 to 9: ")
        if Pmove=="" or Pmove.isdigit()==False: #checks if the move is empty or not a number
            invalidMessage()
            updBoard() 
            cvp()
        #it converts it to an int to be used
        Pmove=int(Pmove)
        if Pmove>9 or Pmove<1: #if the move is out of range, it is invalid
            os.system('cls')
            invalidMessage()
            updBoard()
            cvp()
    if board[Pmove-1]!=X and board[Pmove-1]!=O: #checks if the space is empty
        if turn==1: #checks whose turn it is
            board[Pmove-1]=X #changes the board and then changes the turn
            turn=2
            if checkWin(X): #checks if the player has won, if they have, it clears the screen and prints the winner
                clr()
                print("Player 1 wins!")
                input("Press enter to exit")
                raise SystemExit     #exits the game as there is no more code to run
            Pmove=2
            cvp() #calls the function again to continue the game
        else: #computers turn
            middle()
            canwin(O)
            if checkWin(O): #checks if the player has won, if they have, it clears the screen and prints the winner
                clr()
                print("Computer wins!")
                input("Press enter to exit")
                raise SystemExit
            canwin(X)
            if turn==2:
                turn=1
                cvp()
            else:
                while True:
                    Cmove=random.randint(0,8)
                    if board[Cmove]!=X and board[Cmove]!=O:
                        board[Cmove]=O
                        turn=1
                        if checkWin(O):
                            clr()
                            print("Computer wins!")
                            input("Press enter to exit")
                            raise SystemExit
                        cvp()
                    else: #if the space is already taken, it will try again
                        continue



         
    else: #if the space is already taken, it is invalid
        clr()
        invalidMessage()
    updBoard()
while True:
    clr() #clears the screen at the start
    input("Welcome to Tic Tac Toe! Press enter to start") #welcome message
    pInput=input("press p for player vs player, or c for computer vs player") #game mode selection #infinite loop to keep the game running until a gamemode is selected
    if (pInput=="p"):
        pvp() #if the input is not p, it will exit the game
        break
    elif(pInput=="c"):
        cvp()
        break
    else:
        input("press enter to try again")
        continue


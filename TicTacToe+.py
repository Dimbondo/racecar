import os  # used to clear the screen
import random  # used for the computer to make random moves

os.system("cls")  # clears the screen at the start


# variables for the game
X = "\033[31mX\033[0m"
O = "\033[34mO\033[0m"
turn = 1
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# _______________________ FUNCTIONS__________________________
# function to clear the screen
def clr():
    os.system("cls")


# function to print invalid input message
def invalidMessage():
    clr()
    print("Invalid input")
    input("Press enter to continue")


# counts the amount of empty spaces, if there are none and no player wins, it is a draw
def checkDraw():
    if checkWin(X) or checkWin(O):
        return  # Don't consider it a draw if someone already won

    count = 0
    for i in range(9):
        if board[i] != X and board[i] != O:
            count += 1
    if count == 0:
        clr()
        print("Draw!")
        input("Press enter to exit")
        raise SystemExit


# checks if a player has won by checking all possible winning combinations
def checkWin(player):
    count = 0
    for i in range(3):
        # horizontal wins
        if (
            board[count] == player
            and board[count + 1] == player
            and board[count + 2] == player
        ):
            return True
        count += 3
    count = 0
    for i in range(3):
        # vertical wins
        if (
            board[count] == player
            and board[count + 3] == player
            and board[count + 6] == player
        ):
            return True
        count += 1
        # diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True


# clears the board and prints the board based on the list
def updBoard():
    clr()
    global board
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("--+---+--")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("--+---+--")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))


# player vs player mode
def pvp():
    global turn, board
    board[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = 1
    while True:

        updBoard()
        checkDraw()
        print(f"Player {turn}'s turn!")  # prints whose turn it is
        move = input("Enter a number from 1 to 9: ")
        # before any real gameplay, the input is checked to see if its valid
        if (
            move == "" or not move.isdigit()
        ):  # checks if the move is empty or not a number
            invalidMessage()
            updBoard()
            continue
        # it converts it to an int to be used
        move = int(move)

        if move > 9 or move < 1:  # if the move is out of range, it is invalid
            clr()
            invalidMessage()
            updBoard()
            continue

        if (
            board[move - 1] != X and board[move - 1] != O
        ):  # checks if the space is empty
            # player 1 gameplay
            if turn == 1:
                board[move - 1] = X  # changes the board and then changes the turn
                turn = 2
                if checkWin(
                    X
                ):  # checks if the player has won, if they have, it clears the screen and prints the winner
                    clr()
                    updBoard()
                    print("Player 1 wins!")
                    input("Press enter to exit")
                    raise SystemExit  # exits the game as there is no more code to run
                continue  # continue instead of calling the function, since that resets the games progress!

            else:  # same thing as above, but for player 2
                board[move - 1] = O
                turn = 1
                if checkWin(O):
                    clr()
                    updBoard()
                    print("Player 2 wins!")
                    input("Press enter to exit")
                    raise SystemExit
                continue
        else:  # if the space is already taken, it is invalid
            clr()
            updBoard()
            invalidMessage()
            continue


# _____________________________________________________________________________________________________________________
# cvp functions and game
def canwin(i):  # checks if the player can win in the next move
    global board, turn
    for j in range(9):
        if board[j] != O and board[j] != X:
            board[j] = i
            if checkWin(i):
                if i == X:
                    turn = (
                        1  # if the player can win, it changes the turn to the computer
                    )
                board[j] = O
                return
            board[j] = j + 1  # if the player cannot win, it resets the space


def middle():
    # Checks if middle square is open, but like why does it prioritize the middle square?
    global board, turn
    if board[4] != X and board[4] != O:
        board[4] = O
        turn = 1


def cvp():
    global turn, board
    board[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn = 1  # Reset turn each time cvp is called

    while True:
        updBoard()
        checkDraw()

        if turn == 2:
            # Computer's move
            middle()
            canwin(O)
            if checkWin(O):
                clr()
                print("Computer wins!")
                input("Press enter to exit")
                raise SystemExit

            canwin(X)
            if turn == 1:
                continue  # blocked player, now wait for player's move

            # Random move if no winning/blocking move
            while True:
                Cmove = random.randint(0, 8)
                if board[Cmove] != X and board[Cmove] != O:
                    board[Cmove] = O
                    turn = 1
                    if checkWin(O):
                        clr()
                        print("Computer wins!")
                        input("Press enter to exit")
                        raise SystemExit
                    break  # valid move, continue game
        else:
            # Player's turn
            print("Player 1's turn")
            Pmove = input("Enter a number from 1 to 9: ")

            if Pmove == "" or not Pmove.isdigit():
                invalidMessage()
                continue

            Pmove = int(Pmove)
            if Pmove < 1 or Pmove > 9:
                invalidMessage()
                continue

            if board[Pmove - 1] == X or board[Pmove - 1] == O:
                invalidMessage()
                continue

            board[Pmove - 1] = X
            if checkWin(X):
                clr()
                print("Player 1 wins!")
                input("Press enter to exit")
                raise SystemExit

            turn = 2  # now computer's turn


def game_start():
    while True:
        clr()
        input("Welcome to Tic Tac Toe! Press Enter to start.")
        mode = input(
            "Press [p] for Player vs Player, or [c] for Computer vs Player: "
        ).lower()

        if mode == "p":
            pvp()
            break
        elif mode == "c":
            cvp()
            break
        else:
            input("Invalid input. Press Enter to try again.")


# Call the function to start the game
game_start()

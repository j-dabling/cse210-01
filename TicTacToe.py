# CSE 210 - W02 Prove Submission - Tic Tac Toe
# Author - Jacob Dabling

from colorama import Fore, Style

def main():
    board = [["1", "|", "2", "|", "3"],
            ["-", "+", "-", "+", "-"],
            ["4", "|", "5", "|", "6"],
            ["-", "+", "-", "+", "-"],
            ["7", "|", "8", "|", "9"]]
    print("Welcome! Press the number of the square you'd like to place on.")
    print("Then press ENTER")
    
    key = ' '
    team = True # true is for X team, and false for O team.
    while key != 'q':
        # Checks to see if the game has been won.
        if checkGameWin(board):
            outputBoard(board, team)
            print("Congradulations! You won!")
            break;
        else:
            team = not team

        outputBoard(board, team)
        
        # Tell the players who's turn it is.
        if team:
            print("\33[31mPlayer X's turn!")
        else:
            print("\33[32mPlayer O's turn!")

        # Get ready to accept user input.
        key = input("Box number: ")
        print("\n")
        if(key=='1'):
            board = editSpace(board, (0,0), team)
        elif(key=='2'):
            board = editSpace(board, (0,2), team)
        elif(key=='3'):
            board = editSpace(board, (0,4), team)
        elif(key=='4'):
            board = editSpace(board, (2,0), team)
        elif(key=='5'):
            board = editSpace(board, (2,2), team)
        elif(key=='6'):
            board = editSpace(board, (2,4), team)
        elif(key=='7'):
            board = editSpace(board, (4,0), team)
        elif(key=='8'):
            board = editSpace(board, (4,2), team)
        elif(key=='9'):
            board = editSpace(board, (4,4), team)
        
        
# Checks the game board to see if a player has won.
def checkGameWin(board):
    # Check first for horizontal victories.
    if board[0][0] == board[0][2] == board[0][4]:
        return True
    elif board[2][0] == board[2][2] == board[2][4]:
        return True
    elif board[4][0] == board[4][2] == board[4][4]:
        return True
    
    # Then check for vertical victories.
    elif board[0][0] == board[2][0] == board[4][0]:
        return True
    elif board[0][2] == board[2][2] == board[4][2]:
        return True
    elif board[0][4] == board[2][4] == board[4][4]:
        return True

    # Then check for diagonals.
    elif board[0][0] == board[2][2] == board[4][4]:
        return True
    elif board[4][0] == board[2][2] == board[0][4]:
        return True
    
    # If no victory conditions are met, return false.
    return False

# Given a space on the board, insert the appropriate symbol.
def editSpace(board, space, team):
    if team:
        board[space[0]][space[1]] = 'X'
    else:
        board[space[0]][space[1]] = 'O'
    return board

# Prints the current state of the board to the console.
def outputBoard(board, team):
    i = 0
    for row in board:
        if(i%2 == 0):
            print(" ".join(row))
        else:
            print("-".join(row))
        i += 1

main()
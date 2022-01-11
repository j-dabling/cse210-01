# CSE 210 - W02 Prove Submission - Tic Tac Toe
# Author - Jacob Dabling

#import keyboard

def main():
    board = [["1", "|", "2", "|", "3"],
            ["-", "-", "-", "-", "-"],
            ["4", "|", "5", "|", "6"],
            ["-", "-", "-", "-", "-"],
            ["7", "|", "8", "|", "9"]]
    outputBoard(board)
    print("Welcome! Press the number of the square you'd like to place on.")
    print("Then press ENTER")
    
    key = ' '
    team = True # true is for X team, and false for O team.
    while key != 'q':
        key = input()
        if(key=='1'):
            board = editSpace(board, (0,0), team)
            team = not team
            outputBoard(board)
        elif(key=='2'):
            board = editSpace(board, (0,2), team)
            team = not team
            outputBoard(board)
        elif(key=='3'):
            board = editSpace(board, (0,4), team)
            team = not team
            outputBoard(board)
        elif(key=='4'):
            board = editSpace(board, (2,0), team)
            team = not team
            outputBoard(board)
        elif(key=='5'):
            board = editSpace(board, (2,2), team)
            team = not team
            outputBoard(board)
        elif(key=='6'):
            board = editSpace(board, (2,4), team)
            team = not team
            outputBoard(board)
        elif(key=='7'):
            board = editSpace(board, (4,0), team)
            team = not team
            outputBoard(board)
        elif(key=='8'):
            board = editSpace(board, (4,2), team)
            team = not team
            outputBoard(board)
        elif(key=='9'):
            board = editSpace(board, (4,4), team)
            team = not team
            outputBoard(board)

def editSpace(board, space, team):
    if team:
        board[space[0]][space[1]] = 'X'
    else:
        board[space[0]][space[1]] = 'O'
    return board

# Prints the current state of the board to the console.
def outputBoard(board):
    i = 0
    for row in board:
        if(i%2 == 0):
            print(" ".join(row))
        else:
            print("-".join(row))
        i += 1

main()
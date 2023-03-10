"""
Simple tic tac toe game?!
"""

BOARD = [[" "] * 3 for x in range(3)]


def print_board(board):
    ends = "  +-+-+-+"
    print("   1 2 3 ")
    print(ends)
    num = 1
    for row in board:
        print("%d |%s|" % (num, "|".join(row)))
        print(ends)
        num += 1


def get_move():
    while True:
        user_row = input("Enter the row: ").strip()
        if user_row not in "123":
            print("Enter a valid number!")
        elif user_row == "":
            print("Enter a number.")
        while True:
            user_col = input("Enter the col: ").strip()
            if user_col not in "123":
                print("Enter a valid number!")
            elif user_col == "":
                print("Enter a number.")
            break
        break
    
    user_move = int(user_row), int(user_col)
    print(user_move)
    check_move(user_move)


def check_move(user_move):
    row, col = user_move
    if BOARD[row][col] == " ":
        BOARD[row][col] = "X"
    elif BOARD[row][col] != " ":
        print("That's already taken...")
        get_move()


def start_game():
    print("")


get_move()
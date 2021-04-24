import os
import string
import random
import sys

alphabet = string.ascii_uppercase

numbers = string.digits[1:]

EMPTY_FIELD = '#'

def coordinates_dict(height, width):
    coordinates_dict = {}
    for i in range(height):
        for j in range(width):
            coordinates_dict[alphabet[i]+str(j+1)]=i,j
    return coordinates_dict

def generate_board(height, width):
        if height * width > len(alphabet) * 2:
            raise ValueError("The table is oversized!")
        if height * width % 2 != 0:
            raise ValueError("The amount of the board areas must be even!")

        temp_board=sorted(alphabet*2)[:height*width]

        board= [["#" for i in range(width)] for j in range(height)]

        for i in range(height):
            for j in range(width):
                temp_elem = random.choice(temp_board)
                board[i][j]=temp_elem
                temp_board.remove(temp_elem)
        return board

def generate_active_board(height, width):
    active_board= [["#" for i in range(width)] for j in range(height)]
    return active_board


def print_board(board):
    print(" ", " ".join(alphabet[i] for i in range(len(board[0]))))
    for col, row in zip(numbers, board):
        print(col, " ".join(row))

# clears the screen
def console_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_coordinate(LETTERNUMBER, active_board):
    while True:
        user_input = input("Please provide coordinates like B2:")
        if is_valid_input(user_input, LETTERNUMBER, active_board):
            user_coordinates = LETTERNUMBER[user_input.upper()]
            return user_coordinates
        else:
            print("\nInvalid input!\n")

def is_valid_input(user_input, LETTERNUMBER, active_board):
    col, row = (LETTERNUMBER[user_input.upper()])
    if user_input.upper() in LETTERNUMBER.keys() and active_board[row][col] == EMPTY_FIELD:
        return True
    else:
        False

def choose_difficulty_level():
    is_looping = True
    while is_looping:
        difficulty_level = input("Please provide difficult level: 1 - easy, 2 - medium, 3 - hard: ")
        if difficulty_level in ["1", "2", "3"]:
            is_looping = False
        else:
            print("\nYour input is incorrect!\n")

    if difficulty_level == "1":
        height = 5
        width = 4
    elif difficulty_level == "2":
        height = 5
        width = 6
    elif difficulty_level == "3":
        height = 5
        width = 10

    return height, width


def main():
    print("Welcome to Memory Game!\n")
    height, width = choose_difficulty_level()
    board = generate_board(height, width)
    active_board = generate_active_board(height, width)
    LETTERNUMBER = coordinates_dict(height, width)
    step = 1
    
    while True:
        print(f"\nThe step number: {step}.\n")
        print_board(active_board)
        col_1, row_1  = get_coordinate(LETTERNUMBER, active_board)
        active_board[row_1][col_1] = board[row_1][col_1]
        print_board(active_board)
        col_2, row_2 = get_coordinate(LETTERNUMBER, active_board)
        active_board[row_2][col_2] = board[row_2][col_2]
        print_board(active_board)
        if active_board[row_1][col_1] != active_board[row_2][col_2]:
            active_board[row_1][col_1] = EMPTY_FIELD
            active_board[row_2][col_2] = EMPTY_FIELD
            print("\nOhhhhhhhh, You missed!\n")
        else: 
            print("\nGreat shot!\n")
        print_board(active_board)

        found_empty_field = False

        for row in active_board:
            if EMPTY_FIELD in row:
                found_empty_field = True
                break
        if not found_empty_field:
            print(f"This is the end of the game! You finished it in {step} steps!")
            sys.exit()

        step += 1

if __name__ == "__main__":
    main()
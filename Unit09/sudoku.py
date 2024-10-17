"""Dessa Shapiro"""
import time
import math 
import random
#prints the board
def print_board(board):
    RED = "\033[31m"
    BLACK = "\033[37m"
    
    N = len(board)
    n = math.floor(math.sqrt(N))
    assert N == n*n

    board_string = ""
    for row in range(N):
        if row > 0 and row % n == 0:
            board_string += "\n"
        for col in range(N):
            if col > 0 and col % n == 0: 
                board_string += " "
            value = board[row][col]
            if value != 0:
                board_string += RED
            else:
                board_string += BLACK
            board_string += "[{:02.0f}]".format(value)
            
        board_string += "\n" + BLACK

    print(board_string)

#Makes a puzzle using rows and columns 
def make_puzzle(N):
    board = [[0] * N for _ in range(N)]
    row_sets = [set() for _ in range(N)]
    col_sets = [set() for _ in range(N)]
    n = int(math.sqrt(N))
    reg_sets = [[set() for _ in range(n)] for _ in range(n)]

    for _ in range(N):
        while True:
            row = random.randint(0, N - 1)
            col = random.randint(0, N - 1)
            num = random.randint(1, N)
            re_row, re_col = row // n, col // n
            if num not in row_sets[row] and num not in col_sets[col] and num not in reg_sets[re_row][re_col]:
                
                
                board[row][col] = num
                row_sets[row].add(num)
                col_sets[col].add(num)
                reg_sets[re_row][re_col].add(num)
                break
    return {'board': board, 'row_sets': row_sets, 'col_sets': col_sets, 'reg_sets': reg_sets}

#selects one square from the puzzle board 
def get_square(puzzle, row, col):
    value = puzzle['board'][row][col]
    row_set = puzzle['row_sets'][row]
    col_set = puzzle['col_sets'][col]
    reg_set = puzzle['reg_sets'][row // int(len(puzzle['board']) ** 0.5)][col // (int(len(puzzle['board']) ** 0.5))]

    square = {'value': value,'row_set': row_set,'col_set': col_set,'reg_set': reg_set}

    return square

#The function checks the placeing and if the move is valud it updates and returns True
#move runs in constant time 
def move(puzzle, row, col, new_value):
    square_info = get_square(puzzle, row, col)
    if square_info['value'] == 0 and new_value not in square_info['row_set'] and new_value not in square_info['col_set'] and new_value not in square_info['reg_set']:
        puzzle['board'][row][col] = new_value
        square_info['row_set'].add(new_value)
        square_info['col_set'].add(new_value)
        square_info['reg_set'].add(new_value)
        return True
    return False

#Fills the puzzle with random values and make sure it remains valid
#Fill puzzle runs in N^4 time complexity becuase the iteration 
def fill_puzzle(puzzle):
    N = len(puzzle['board'])
    max_attempts = N ** 4
    filled = 0
    target = int(0.75 * math.sqrt(N))
    while filled < max_attempts and filled < target:
        row = random.randint(0, N-1)
        col = random.randint(0, N-1)
        numb = random.randint(1, N)

        move(puzzle, row, col, numb)
        filled += 1

#calls the puzzle and checks time complexity 
def main():
    N = 16
    print("Board size:", N, "x", N)
    puzzle = make_puzzle(N)
    print("Initial puzzle:")
    print(puzzle)
    print("Initial board:")
    print_board(puzzle['board'])

    start = time.perf_counter()
    fill_puzzle(puzzle)
    end = time.perf_counter()

    print("Final puzzle:")
    print(puzzle)
    print("Final board:")
    print_board(puzzle['board'])
    print("Total time:", end - start)

#everything runs here
if __name__ == "__main__":
    main()

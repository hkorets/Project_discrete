'''sudoku mark3 module'''

import copy

def printing_sudoku(arr):
    '''function for string representation of sudoku'''
    for i in range(9):
        if i in (3, 6):
            print('-------------------')
        for j in range(9):
            if j in (3, 6):
                print('|', end='')
            print(arr[i][j], end = " ")
        print()

def find_next_empty_space(field):
    '''function for checking if the grid has
    any space for the next move'''
    for i in range(9):
        for j in range(9):
            if field[i][j] == 0:
                return (i, j)
    return None

def solve_backtracking(field):
    '''function for solving the sudoku puzzle'''
    if (coords := find_next_empty_space(field)) is None:
        return True                # if there are no blank spots, the sudoku is solved

    row, col = coords              # grab the coordinates of the next blank spot

    for num in range(1, 10):
        if valid_move(field, row, col, num):
            field[row][col] = num
            if solve_backtracking(field):
                return True        # for the suitable numbers, solve using backtracking
            field[row][col] = 0
    return False                   # if no numbers are right for the box, sudoku is unsolvable

def validate_field(field):
    '''function for validation of the given field'''
    valid = True
    for i in range(9):
        for j in range(9):
            num = field[i][j]
            if num != 0:          # for every number in the field, check if it doesnt break the rules
                field[i][j] = 0
                valid = valid and valid_move(field, i, j, num)
                field[i][j] = num
    return valid

def valid_move(field, row, col, num):
    '''function for validating the next move'''
    for x in range(9):            # checking all rows for the same number
        if field[row][x] == num:
            return False

    for x in range(9):            # checking all columns for the same number
        if field[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):            # checking the 3 by 3 box for the same number
        for j in range(3):
            if field[i + start_row][j + start_col] == num:
                return False
    return True                   # if all the checks are passed, the move is valid

def logical_fill(field):
    '''function for filling the field only with numbers that are 100% right'''
    premove = None                # creating variable to save how the field looks before iteration
    while premove != field:       # making a cycle that will stop when the iteration doesn't do anything
        premove = copy.deepcopy(field)    # saving the field
        for row in range(9):
            for col in range(9):
                if field[row][col] > 0:
                    continue

                possible = []            # list for all numbers that can be put in this box

                for num in range(1, 10):

                    if valid_move(field, row, col, num):
                        possible.append(num)   # saving all the possible moves in the list

                if len(possible) == 1:         # if the box has only one possible move, it means it is 100% right
                    field[row][col] = possible[0]
                else:
                    continue                   # skip the boxes that arent 100% solvable on current iteration
    return None

def sudoku(field):
    '''function for solving given sudoku'''
    if validate_field(field):       # validating the given field
        logical_fill(field)         # making all the moves that are 100% right to shorten the cycles
        return solve_backtracking(field)    # solving the rest using backtracking
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if sudoku(grid):
    printing_sudoku(grid)
else:
    print("no solution  exists ")


# ? реалізувати клас для розв'язку, щоб програма мала зручний функціонал

# ? додати аргумент з допустимим відсотком помилки
# при пробі підставити для обмеження глибини бектрекінгу

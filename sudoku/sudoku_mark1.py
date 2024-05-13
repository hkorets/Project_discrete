'''sudoku module'''

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

def valid_move(field, row, col, num):
    '''function for validating the next move'''
    for x in range(9):            # checking all the rows for the same number
        if field[row][x] == num:
            return False

    for x in range(9):            # checking all the columns for the same number
        if field[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):            # checking the 3 by 3 box for the same number
        for j in range(3):
            if field[i + start_row][j + start_col] == num:
                return False
    return True                   # if there are no same numbers, the move is valid

def solve(field):
    '''function for solving the sudoku puzzle'''
    if (coords := find_next_empty_space(field)) is None:
        return True               # if there are no empty spaces anymore, sudoku is solved

    row, col = coords

    if field[row][col] > 0:       # if given space is already occupied, move on using recursion
        return solve(field)

    for num in range(1, 10):      # try all the numbers for the given space

        # possible = []

        if valid_move(field, row, col, num):
            field[row][col] = num    # if the move is valid, we try to solve the sudoku with it
            if solve(field):         # if we find solution, return True for solved sudoku
                return True
            field[row][col] = 0      # if its unsolvable with this move
                                     # reverse it and try a different one (backtracking)

            # possible.append(num)
    # if len(possible) == 1:
    #     field[row][col] = possible[0]
    # else:
    #     if col != 9:
    #         return solve(field, row, col+1)
    #     return solve(field, row+1, 0)

    return False                 # if no numbers are suitable, return False for unsolvable puzzle

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solve(grid):
    printing_sudoku(grid)
else:
    print("no solution  exists ")

# додати перевірку на валідність переданого поля
# придумати алгоритм для зацикленого вставляння цифр які 100% попадають в клітинку
# додати аргумент з допустимим відсотком помилки при пробі підставити

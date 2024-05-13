'''sudoku mark2 module (failed)'''

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
    print()

def check_empty_space(field):
    '''function for checking if the grid has
    any space for the next move'''
    return 0 in sum(field, start=[])
    # for i in range(9):
    #     for j in range(9):
    #         if field[i][j] == 0:
    #             return (i, j)
    # return None

def valid_move(field, row, col, num):
    '''function for validating the next move'''
    for x in range(9):
        if field[row][x] == num:
            return False

    for x in range(9):
        if field[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if field[i + start_row][j + start_col] == num:
                return False
    return True

def solve(grid, row, col):
    '''function for solving the sudoku puzzle'''
    if (row == 8 and col == 9):
        # return True
        row, col = 0, 0

    if not check_empty_space(grid):
        return True

    if col == 9:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    possible = [num for num in range(1, 10) if valid_move(grid, row, col, num)]
    if len(possible) == 1:
        grid[row][col] = possible[0]
        printing_sudoku(grid)
    solve(grid, row, col+1)
    # for num in possible:
    #     grid[row][col] = num
    #     if solve(grid, row, col + 1):
    #         return True
    #     grid[row][col] = 0
    # return False

    # for num in range(1, 10):
    #     if valid_move(grid, row, col, num):
    #         possible.append(num)
    # if len(possible) == 0:
    #     return False
    # if len(possible) == 1:
    #     grid[row][col] = possible[0]
    # return solve(grid, row, col+1)
    #     #     grid[row][col] = num
    #     #     if solve(grid, row, col + 1):
    #     #         return True
    #     # grid[row][col] = 0
    # # return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solve(grid, 0, 0):
    printing_sudoku(grid)
else:
    print("no solution  exists ")

# !!! спроба безкінечного циклу через поле провалилась через обмеження глибини рекурсії


# переробити цикл на for/while, щоб уникнути рекурсії
# після розставляння всіх 100% цифр запускати бектрекінг

'''sudoku in class module'''

import copy
import time

class Sudoku:
    '''class for sudoku puzzles'''

    def __init__(self, field):
        self.field = field

    def __str__(self):
        '''method for string representation of the puzzle'''
        res = ''
        for i in range(9):
            if i in (3, 6):
                res += '-------------------\n'
            for j in range(9):
                if j in (3, 6):
                    res += '|'
                res += str(self.field[i][j]) + ' '
            res += '\n'
        return res

    def find_next_empty_space(self):
        '''method for checking if the grid has
        any space for the next move'''
        for i in range(9):
            for j in range(9):
                if self.field[i][j] == 0:
                    return (i, j)
        return None

    def validate_field(self):
        '''method for validation of the given field'''
        valid = True
        for i in range(9):
            for j in range(9):
                num = self.field[i][j]
                if num != 0:
                    self.field[i][j] = 0
                    valid = valid and self.valid_move(i, j, num)
                    self.field[i][j] = num
        return valid

    def valid_move(self, row, col, num):
        '''function for validating the next move'''
        for x in range(9):
            if self.field[row][x] == num:
                return False

        for x in range(9):
            if self.field[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.field[i + start_row][j + start_col] == num:
                    return False
        return True

    def backtracking_fill(self):
        '''method for filling in the sudoku puzzle'''
        if (coords := self.find_next_empty_space()) is None:
            return True

        row, col = coords

        for num in range(1, 10):

            if self.valid_move(row, col, num):
                self.field[row][col] = num
                if self.backtracking_fill():
                    return True
                self.field[row][col] = 0

        return False

    def logical_fill(self):
        '''method for filling the field only with numbers that are 100% right'''
        premove = None
        while premove != self.field:
            premove = copy.deepcopy(self.field)
            for row in range(9):
                for col in range(9):
                    if self.field[row][col] > 0:
                        continue

                    possible = []

                    for num in range(1, 10):

                        if self.valid_move(row, col, num):
                            possible.append(num)

                    if len(possible) == 1:
                        self.field[row][col] = possible[0]
                    else:
                        continue

    def solve_backtracking(self):
        '''method for solving sudoku only using backtracking'''
        presolve = copy.deepcopy(self.field)
        if self.backtracking_fill():
            return str(self)
        self.field = presolve
        return "No solution exists!"

    def solve_logical(self):
        '''method for logically solving the sudoku'''
        if self.validate_field():
            self.logical_fill()
            return self.solve_backtracking()
        return "The field is invalid!"



grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

start_backtracking = time.time()

for _ in range(100):
    s = Sudoku(grid)
    s.solve_backtracking()

end_backtracking = time.time()

start_logical = time.time()

for _ in range(100):
    s = Sudoku(grid)
    s.solve_logical()

end_logical = time.time()

print(f'Backtracking method time: {end_backtracking - start_backtracking}')
print(f'Logical method time: {end_logical - start_logical}')

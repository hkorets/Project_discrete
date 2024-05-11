"""Crossword solver"""
def is_safe(crossword, word, row, col, direction):
    """
    Check is it safe into put word in crossword
    """
    if direction == 'down':
        for c_row, c_word in zip(range(row, row + len(word)), word):
            if c_row >= len(crossword) or (crossword[c_row][col] != '-' \
                and crossword[c_row][col] != c_word):
                return False
    elif direction == 'across':
        for c_col, c_word in zip(range(col, col + len(word)), word):
            if c_col >= len(crossword[0]) or (crossword[row][c_col] != \
                '-' and crossword[row][c_col] != c_word):
                return False
    return True

def fill_word(crossword, word, row, col, direction):
    """
    puts the word
    """
    if direction == 'down':
        for c_row, c_word in zip(range(row, row + len(word)), word):
            crossword[c_row][col] = c_word
    elif direction == 'across':
        for c_col, c_word in zip(range(col, col + len(word)), word):
            crossword[row][c_col] = c_word

def crossword_solver(crossword, words, index):
    """
    Solve crossword.
    """
    solutions = []
    def backtrack(crossword, words, index, solutions):
        if index == len(words):
            solutions.append([row[:] for row in crossword])
            return
        for i in range(len(crossword)):
            for j in range(len(crossword[0])):
                for direction in ['down', 'across']:
                    if is_safe(crossword, words[index], i, j, direction):
                        fill_word(crossword, words[index], i, j, direction)
                        backtrack(crossword, words, index + 1, solutions)
                        fill_word(crossword, '-' * len(words[index]), i, j, direction)
                        crossword = [row[:] for row in crossword]
    backtrack(crossword, words, index, solutions)
    return solutions


if __name__ == "__main__":
    matrix = []
    matrix.append(['*','-' , '*' , '*' ,'*' , '*','*','*','*','*'])
    matrix.append(['*','-','*','*','*','*','*','*','*','*'])
    matrix.append(['*','-','*','*','*','*','-','*','*' , '*'])
    matrix.append(['*','-','-','*','*','*','-','-','*','*'])
    matrix.append(['*','-','*','*','*','*','-','*','*','*'])
    matrix.append(['*','-','*','*','*','*','-','*','*','*'])
    matrix.append(['*','-','*','*','*','*','-','*','*','*'])
    matrix.append(['*','-','*','-','-','-','-','-','-' , '*'])
    matrix.append(['*','-','*','*','*','*','*','*','*','*'])
    matrix.append(['*','*','*','-','-','-','-','-','-','-'])
    words = ["PUNJAB", "JHARKHAND", "MIZORAM", "MUMBAI"]

    solutions = crossword_solver(matrix, words, 0)
    if solutions:
        print("All solutions:")
        for idx, solution in enumerate(solutions, 1):
            print(f"Solution {idx}:")
            for row in solution:
                print(''.join(row))
            print()
    else:
        print("It is impossible to find a solution!")

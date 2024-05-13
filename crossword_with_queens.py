def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board, col, n, queens_to_place, solutions):
    if queens_to_place == 0:
        solutions.append([row[:] for row in board])
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n, queens_to_place - 1, solutions)
            board[i][col] = 0



def print_board(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print("♛", end=" ")
            else:
                print("_", end=" ")
        print()


def place_queens(n, queens_to_place):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, queens_to_place, solutions)
    if not solutions:
        return "неможливо розставити королеви"
    return solutions


board_size = 8
queens_to_place = 8
result = place_queens(board_size, queens_to_place)
if isinstance(result, str):
    print(result)
else:
    for i, solution in enumerate(result, 1):
        print(f"Варіант {i}:")
        print_board(solution)
        print()

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


def solve_n_queens(board, col, n, queens_to_place):
    if queens_to_place == 0:
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n, queens_to_place - 1):
                return True
            board[i][col] = 0
    return False


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
    if not solve_n_queens(board, 0, n, queens_to_place):
        return "неможливо розставити королеви"
    print_board(board)


board_size = int(input("розмір поля: "))
queens_to_place = int(input("кількість королев: "))
print(place_queens(board_size, queens_to_place))

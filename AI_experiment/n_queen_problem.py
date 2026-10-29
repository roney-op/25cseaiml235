def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    if row == n:
        for i in range(n):
            print("Queen", i + 1, ": Row =", i + 1, "Column =", board[i] + 1)
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


n = int(input("Enter the value of N: "))

board = [-1] * n

solve(board, 0, n)
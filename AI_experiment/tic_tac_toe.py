def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


board = [[" " for _ in range(3)] for _ in range(3)]
player = "X"

for turn in range(9):
    print("\nCurrent Board:")
    print_board(board)
    print(f"Player {player}'s turn")

    while True:
        row = int(input("enter row(0-2):"))
        col = int(input("enter column(0-2):"))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            break
        print("Invalid move. Try again.")

    board[row][col] = player

    if check_winner(board, player):
        print("\nCurrent Board:")
        print_board(board)
        print(f"Player {player} wins!")
        break

    player = "O" if player == "X" else "X"
else:
    print("\nCurrent Board:")
    print_board(board)
    print("it's a draw!")
def print_board(board):
    for row in board:
        print(" ".join(row))

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = player

            if check_winner(board, player):
                print_board(board)
                print(f"Player {player} wins!")
                break
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

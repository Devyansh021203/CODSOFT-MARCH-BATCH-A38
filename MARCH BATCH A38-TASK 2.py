import math

# Constants to represent empty, player X, and player O
EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if the game is over
def game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    # Check if the board is full (tie)
    if all(cell != EMPTY for row in board for cell in row):
        return 'Tie'
    return None

# Function to evaluate the board
def evaluate(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 1 if board[i][0] == PLAYER_X else -1
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 1 if board[0][i] == PLAYER_X else -1
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 1 if board[0][0] == PLAYER_X else -1
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 1 if board[0][2] == PLAYER_X else -1
    # If no winner, return 0
    return 0

# Function for the AI player using Minimax with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    result = game_over(board)
    if result is not None:
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI player
def find_best_move(board):
    best_eval = float('-inf')
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False, alpha, beta)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    current_player = PLAYER_X

    while True:
        print_board(board)

        # Check if the game is over
        result = game_over(board)
        if result is not None:
            if result == 'Tie':
                print("It's a tie!")
            else:
                print(f"{result} wins!")
            break

        # Get the next move from the current player
        if current_player == PLAYER_X:
            row, col = find_best_move(board)
            print("AI plays:", row, col)
        else:
            while True:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == EMPTY:
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Try again.")
        board[row][col] = current_player

        # Switch players
        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    play_game()

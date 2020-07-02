import time
import copy


# Return starting state of the board
def initial_state():
    return [[None, None, None],
            [None, None, None],
            [None, None, None]]

# Return player who has the next turn on a board
def player(board):
    next_turn = 0
    for row in board:
        next_turn += row.count("X")
        next_turn -= row.count("O")
    return "X" if next_turn <= 0 else "O"

# Return (i, j) from number 1 - 9
def position(move):
    i = int((move - 1) /3)
    j = int((move - 1) % 3)
    return (i, j)

# Return 1 - 9 from number (i, j)
def number(move):
    positions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    return positions.index(move) + 1

# Return (i, j) from number 1 - 9
def actions(board):
    available_positions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == None:
                available_positions.add((row, col))
    return available_positions

# Return the board that results from making move (i, j) on the board
def result(board, action):
    i, j = action
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)
    return new_board

# Return the winner of the game, if there is one
def winner(board):
    if utility(board) == 1:
        return "X"
    if utility(board) == -1:
        return "O"
    return None

# Returns True if game is over, False otherwise
def terminal(board):
    if len(actions(board)) == 0 or winner(board) == "X" or winner(board) == "O":
        return True
    return False

# Return 1 if "X" has won the game, -1 if "O" has won, 0 otherwise
def utility(board):
    # Check each row for a winner
    for row in board:
        if row.count("X") == 3:
            return 1
        if row.count("O") == 3:
            return -1

    # Check vertically for a winner
    for i in range(3):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return 1
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return -1

    # Check for a winner Diagonally from bottom left to top right
    if board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
        return 1
    if board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
        return -1

    # Check for a winner Diagonally from top left to bottom right
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return 1
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return -1

    # tie or no winner return 0
    return 0


# Print utility
def print_board(board):
    ln = len(board)
    display_board = copy.deepcopy(board)
    i = 1
    for row in range(ln):
        for col in range(ln):
            if board[row][col] == None:
                display_board[row][col] = str(i)
            i += 1

    row_1 = "  " + display_board[0][0] + "  |  " + display_board[0][1] + "  |  " + display_board[0][2] + "  "
    row_2 = "  " + display_board[1][0] + "  |  " + display_board[1][1] + "  |  " + display_board[1][2] + "  "
    row_3 = "  " + display_board[2][0] + "  |  " + display_board[2][1] + "  |  " + display_board[2][2] + "  "


    print("     |     |     ")
    print(row_1)
    print("_____|_____|_____")
    print("     |     |     ")
    print(row_2)
    print("_____|_____|_____")
    print("     |     |     ")
    print(row_3)
    print("     |     |     ")


# Searching the best move (max value)
def maximizing(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minimizing(result(board, action)))
    return v

# Searching the best move (min value)
def minimizing(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maximizing(result(board, action)))
    return v

# Minimax Algorithm
def minimax(board):
    # Current Player
    current_player = player(board)

    # Maximizing
    if current_player == "X":
        v = float("-inf")
        for action in actions(board):
            k = minimizing(result(board, action))
            if k > v:
                v = k
                best_action = action
    # Minimizing
    else:
        v = float("inf")
        for action in actions(board):
            k = maximizing(result(board, action))
            if k < v:
                v = k
                best_action = action
    return best_action


# Game Start Here
board = initial_state()

print("\n")
print("Enter the game of Minimax Tic-Tac-Toe")
print("\n")
print("You're going to play against minimax algorithm.")
print(("\n"))
print("Your are player X and computer is O.")
print("\n")

player_id = "X"
computer_id = "O"

# Game Play
while True:
    # Winner check
    if terminal(board):
        print_board(board)
        winner = (winner(board))
        if winner == None:
            print("It's a tie!")
            break
        elif winner == 1:
            print("You win!")
            break
        else:
            print("You lose!")
            break

    # Player turn
    if player(board) == player_id:
        print_board(board)
        available_moves = sorted(list(number(move) for move in actions(board)))
        print("\n")
        print("Available moves : ",  available_moves)
        player_move = int(input("Your turn, choose you move? :  "))
        while player_move not in available_moves:
            player_move = int(input("Your turn, choose you move? :  "))
        print("\n")
        move = position(player_move)
        board = result(board, move)
        print_board(board)
        print("\n")

    # Computer turn
    elif player(board) == computer_id:
        print("Computer turn,  running minimax ...  ")
        move = minimax(board)
        board = result(board, move)
        print("\n")

# ============================================
# Program 2: Rule-Based Tic-Tac-Toe AI (Logic-2)
# ============================================

# 0 = empty, 1 = Human (X), 2 = AI (O)
board = [0,0,0,
         0,0,0,
         0,0,0]

# Winning combinations
win_positions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

# Display board
def print_board():
    symbols = [' ', 'X', 'O']
    print()
    for i in range(0, 9, 3):
        print(" ", symbols[board[i]], "|", symbols[board[i+1]], "|", symbols[board[i+2]])
        if i < 6:
            print(" ---+---+---")
    print()

# Check winner
def check_winner(player):
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# POSSWIN function (from book)
def posswin(player):
    for a, b, c in win_positions:
        line = [board[a], board[b], board[c]]
        if line.count(player) == 2 and line.count(0) == 1:
            return [a, b, c][line.index(0)]
    return -1

# AI logic (Logic-2 rules)
def ai_move():
    # Rule 1: Win
    move = posswin(2)
    if move != -1:
        return move

    # Rule 2: Block opponent
    move = posswin(1)
    if move != -1:
        return move

    # Rule 3: Take center
    if board[4] == 0:
        return 4

    # Rule 4: Take a corner
    for i in [0,2,6,8]:
        if board[i] == 0:
            return i

    # Rule 5: Take a side
    for i in [1,3,5,7]:
        if board[i] == 0:
            return i

# Human move
def human_move():
    while True:
        pos = int(input("Enter position (1-9): ")) - 1
        if 0 <= pos <= 8 and board[pos] == 0:
            return pos
        print("Invalid move. Try again.")

# Main game loop
turn = 0
while True:
    print_board()

    board[human_move()] = 1
    turn += 1

    if check_winner(1):
        print_board()
        print("🎉 You win!")
        break

    if turn == 9:
        print("It's a draw!")
        break

    ai = ai_move()
    board[ai] = 2
    turn += 1

    if check_winner(2):
        print_board()
        print("🤖 AI wins!")
        break

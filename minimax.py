import copy

def minimax(board, depth, is_maximizing, symbol):
    score = evaluate(board, symbol)
    if abs(score) == 10 or depth == 5:
        return score
    
    if is_maximizing:
        best_value = float('-inf')
        for move in get_possible_moves(board):
            new_board = apply_move(board, move, symbol)
            value = minimax(new_board, depth + 1, False, -symbol)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for move in get_possible_moves(board):
            new_board = apply_move(board, move, -symbol)
            value = minimax(new_board, depth + 1, True, -symbol)
            best_value = min(best_value, value)
        return best_value

def evaluate(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return 10 if symbol == 1 else -10
    for col in range(5):
        if all(row[col] == symbol for row in board):
            return 10 if symbol == 1 else -10
    if all(board[i][i] == symbol for i in range(5)):
        return 10 if symbol == 1 else -10
    if all(board[i][4-i] == symbol for i in range(5)):
        return 10 if symbol == 1 else -10
    return 0

def get_possible_moves(board):
    moves = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves

def apply_move(board, move, symbol):
    new_board = copy.deepcopy(board)
    row, col = move
    new_board[row][col] = symbol
    return new_board

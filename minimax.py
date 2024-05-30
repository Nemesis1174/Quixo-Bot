
class Minimax:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def minimax(self, board, depth, alpha, beta, is_maximizing, symbol, opponent_symbol):
        if depth == 0 or self.is_terminal(board):
            return self.heuristic(board, symbol, opponent_symbol)
        
        if is_maximizing:
            max_eval = -float('inf')
            for new_board in self.get_all_moves(board, symbol):
                eval = self.minimax(new_board, depth-1, alpha, beta, False, symbol, opponent_symbol)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for new_board in self.get_all_moves(board, opponent_symbol):
                eval = self.minimax(new_board, depth-1, alpha, beta, True, symbol, opponent_symbol)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def heuristic(self, board, symbol, opponent_symbol):
        # Heurística simple: contar la cantidad de piezas propias y oponentes en el tablero.
        my_count = sum(row.count(symbol) for row in board)
        opponent_count = sum(row.count(opponent_symbol) for row in board)
        return my_count - opponent_count

    def is_terminal(self, board):
        # Verificar si hay una línea completa de símbolo 1 o -1
        for i in range(5):
            if abs(sum(board[i])) == 5 or abs(sum(row[i] for row in board)) == 5:
                return True
        if abs(sum(board[i][i] for i in range(5))) == 5 or abs(sum(board[i][4-i] for i in range(5))) == 5:
            return True
        return False

    def get_all_moves(self, board, symbol):
        # Generar todos los movimientos posibles para el símbolo dado
        moves = []
        for i in range(5):
            for j in range(5):
                if board[i][j] == 0 and (i in [0, 4] or j in [0, 4]):
                    new_board = self.get_board_after_move(board, i, j, symbol)
                    moves.append(new_board)
        return moves

    def get_board_after_move(self, board, row, col, symbol):
        # Generar un nuevo tablero después de mover la pieza desde (row, col) a una nueva posición válida
        new_board = [r[:] for r in board]
        if row == 0:
            for i in range(4, 0, -1):
                new_board[i][col] = new_board[i-1][col]
            new_board[0][col] = symbol
        elif row == 4:
            for i in range(4):
                new_board[i][col] = new_board[i+1][col]
            new_board[4][col] = symbol
        elif col == 0:
            for j in range(4, 0, -1):
                new_board[row][j] = new_board[row][j-1]
            new_board[row][0] = symbol
        elif col == 4:
            for j in range(4):
                new_board[row][j] = new_board[row][j+1]
            new_board[row][4] = symbol
        return new_board



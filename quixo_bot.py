from minimax import Minimax
import os

class QuixoBot:
    def __init__(self, symbol):
        self.name = "QuixoBot"
        self.symbol = symbol
        self.opponent_symbol = -symbol
        self.minimax = Minimax(max_depth=3)

    def play_turn(self, board):
        best_move = None
        best_score = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        
        for i in range(5):
            for j in range(5):
                if self.is_legal_move(i, j, board):
                    new_board = self.get_board_after_move(board, i, j, self.symbol)
                    score = self.minimax.minimax(new_board, self.minimax.max_depth, alpha, beta, False, self.symbol, self.opponent_symbol)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            return self.get_board_after_move(board, best_move[0], best_move[1], self.symbol)
        return board

    def is_legal_move(self, row, col, board):
        invalid_positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        return (row == 0 or row == 4 or col == 0 or col == 4) and (row, col) not in invalid_positions

    def get_board_after_move(self, board, row, col, symbol):
        # Mover la pieza desde (row, col) a una nueva posición válida en el borde de la fila o columna
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

    def print_board(self, board):
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()

    def reset(self, symbol):
        self.symbol = symbol

os.system('cls')

# Creamos el tablero inicial
board = [[0] * 5 for _ in range(5)]
# Inicializamos el bot
bot = QuixoBot(1)

# Hacemos que el bot juegue 5 turnos
for _ in range(5):
    board = bot.play_turn(board)
    bot.print_board(board)


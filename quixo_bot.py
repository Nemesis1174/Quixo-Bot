class QuixoBot:
    def __init__(self, symbol):
        self.name = "QuixoBot"
        self.symbol = symbol
        
    def play_turn(self, board):
        for i in range(5):
            for j in range(5):
                if self.is_legal_move(i, j):
                    # Encuentra el primer movimiento válido y hazlo
                    if i == 0:
                        return self.__move_down(board, i, j)
                    elif i == 4:
                        return self.__move_up(board, i, j)
                    elif j == 0:
                        return self.__move_right(board, i, j)
                    elif j == 4:
                        return self.__move_left(board, i, j)
        return board

    def is_legal_move(self, row, col):
        invalid_positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        if (row == 0 or row == 4 or col == 0 or col == 4) or \
                (row == 0 and col == 0) or \
                (row == 0 and col == 4) or \
                (row == 4 and col == 0) or \
                (row == 4 and col == 4):
            if (row, col) not in invalid_positions:
                return True
        return False

    def __move_right(self, board, row, col, end_col=4):
        new_board = [r[:] for r in board]
        for j in range(end_col, col, -1):
            new_board[row][j] = new_board[row][j-1]
        new_board[row][col] = self.symbol
        return new_board
    
    def __move_left(self, board, row, col, end_col=0):
        new_board = [r[:] for r in board]
        for j in range(end_col, col):
            new_board[row][j] = new_board[row][j+1]
        new_board[row][col] = self.symbol
        return new_board
    
    def __move_up(self, board, row, col, end_row=0):
        new_board = [r[:] for r in board]
        for i in range(end_row, row):
            new_board[i][col] = new_board[i+1][col]
        new_board[row][col] = self.symbol
        return new_board
    
    def __move_down(self, board, row, col, end_row=4):
        new_board = [r[:] for r in board]
        for i in range(end_row, row, -1):
            new_board[i][col] = new_board[i-1][col]
        new_board[row][col] = self.symbol
        return new_board
    
    def print_board(self, board):
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()
    
    def reset(self, symbol):
        self.symbol = symbol

# Creamos el tablero inicial
board = [[0] * 5 for _ in range(5)]
# Inicializamos el bot
bot = QuixoBot(1)

# Hacemos que el bot juegue 10 turnos
for _ in range(5):
    board = bot.play_turn(board)
    bot.print_board(board)


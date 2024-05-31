import random
import copy

class QuixoRandomBot:
    ALLOWED_PIECES_RIGHT = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]
    ALLOWED_PIECES_LEFT = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 1), (4, 2), (4, 3), (4, 4)]
    ALLOWED_PIECES_UP = [(1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    ALLOWED_PIECES_DOWN = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4)]

    def __init__(self, symbol):
        self.name = "QuixoRandomBot"
        self.symbol = symbol
        self.opponent_symbol = -symbol

    def play_turn(self, board):
        valid_moves = []

        for i in range(5):
            for j in range(5):
                if self.is_legal_move(i, j, board):
                    possible_moves = self.get_possible_moves(board, i, j, self.symbol)
                    valid_moves.extend(possible_moves)

        if valid_moves:
            return random.choice(valid_moves)
        return board

    def is_legal_move(self, row, col, board):
        allowed_positions = self.ALLOWED_PIECES_GENERAL
        return (row, col) in allowed_positions and (board[row][col] in [0, self.symbol])

    def get_possible_moves(self, board, row, col, symbol):
        new_boards = []
        if row == 0:
            new_boards.append(self.move_down(copy.deepcopy(board), row, col))
        elif row == 4:
            new_boards.append(self.move_up(copy.deepcopy(board), row, col))
        if col == 0:
            new_boards.append(self.move_right(copy.deepcopy(board), row, col))
        elif col == 4:
            new_boards.append(self.move_left(copy.deepcopy(board), row, col))
        return new_boards

    def move_right(self, board, row, col, end_col=4):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_RIGHT:
            if piece == 0 or piece == self.symbol:
                for i in range(col, end_col):
                    board[row][i] = board[row][i + 1]
                board[row][end_col] = self.symbol
        return board

    def move_left(self, board, row, col, end_col=0):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_LEFT:
            if piece == 0 or piece == self.symbol:
                for i in range(col, end_col, -1):
                    board[row][i] = board[row][i - 1]
                board[row][end_col] = self.symbol
        return board

    def move_up(self, board, row, col, end_row=0):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_UP:
            if piece == 0 or piece == self.symbol:
                for i in range(row, end_row, -1):
                    board[i][col] = board[i - 1][col]
                board[end_row][col] = self.symbol
        return board

    def move_down(self, board, row, col, end_row=4):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_DOWN:
            if piece == 0 or piece == self.symbol:
                for i in range(row, end_row):
                    board[i][col] = board[i + 1][col]
                board[end_row][col] = self.symbol
        return board

    def print_board(self, board):
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()

    def reset(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = -symbol



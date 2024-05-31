import random
import copy

class QuixoRandomBot:
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
        invalid_positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        return (row == 0 or row == 4 or col == 0 or col == 4) and (board[row][col] in [0, self.symbol]) and (row, col) not in invalid_positions

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
        aux = board[row][col]
        for i in range(col + 1, end_col + 1):
            board[row][i-1] = board[row][i]
        board[row][end_col] = aux
        return board

    def move_left(self, board, row, col, end_col=0):
        aux = board[row][col]
        for i in range(col - 1, end_col-1, -1):
            board[row][i+1] = board[row][i]
        board[row][end_col] = aux
        return board

    def move_up(self, board, row, col, end_row=0):
        aux = board[row][col]
        for i in range(row-1, end_row-1, -1):
            board[i+1][col] = board[i][col]
        board[end_row][col] = aux
        return board

    def move_down(self, board, row, col, end_row=4):
        aux = board[row][col]
        for i in range(row + 1, end_row+1):
            board[i-1][col] = board[i][col]
        board[end_row][col] = aux
        return board

    def print_board(self, board):
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()

    def reset(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = -symbol


import copy
from minimax import Minimax, GameNode, GameTree

class QuixoBot:
    ALLOWED_PIECES_RIGHT = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]
    ALLOWED_PIECES_LEFT = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 4), (4, 1), (4, 2), (4, 3), (4, 4)]
    ALLOWED_PIECES_UP = [(1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    ALLOWED_PIECES_DOWN = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4)]
    ALLOWED_PIECES_GENERAL = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

    def __init__(self, symbol):
        self.name = "Chris Bot"
        self.symbol = symbol
        self.opponent_symbol = -symbol
        self.minimax = Minimax(max_depth=2)

    def play_turn(self, board):
        root_node = GameNode(board)
        game_tree = GameTree(root_node)
        game_tree.build_tree(self, depth=2, maximizing_player=True)
        best_move = self.minimax.search_best_move(root_node, self.symbol, self.opponent_symbol)
        return self.apply_move(board, best_move, self.symbol) if best_move else board

    def generate_moves(self, board, symbol):
        moves = []
        allowed_positions = self.ALLOWED_PIECES_GENERAL
        for direction in ['right', 'left', 'up', 'down']:
            for row, col in allowed_positions:
                if board[row][col] == 0 or board[row][col] == symbol:
                    if self.is_valid_move(board, direction, row, col, symbol):
                        moves.append((direction, (row, col)))
        return moves

    def is_valid_move(self, board, direction, row, col, symbol):
        if direction == 'right' and col < 4 and (board[row][col + 1] == 0 or board[row][col + 1] == symbol):
            return True
        if direction == 'left' and col > 0 and (board[row][col - 1] == 0 or board[row][col - 1] == symbol):
            return True
        if direction == 'up' and row > 0 and (board[row - 1][col] == 0 or board[row - 1][col] == symbol):
            return True
        if direction == 'down' and row < 4 and (board[row + 1][col] == 0 or board[row + 1][col] == symbol):
            return True
        return False

    def apply_move(self, board, move, symbol):
        new_board = copy.deepcopy(board)
        direction, (row, col) = move
        if direction == 'right':
            self.move_right(new_board, row, col)
        elif direction == 'left':
            self.move_left(new_board, row, col)
        elif direction == 'up':
            self.move_up(new_board, row, col)
        elif direction == 'down':
            self.move_down(new_board, row, col)
        return new_board

    def move_right(self, board, row, col, end_col=4):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_RIGHT:
            if piece == 0 or piece == self.symbol:
                for i in range(col, end_col):
                    board[row][i] = board[row][i + 1]
                board[row][end_col] = self.symbol

    def move_left(self, board, row, col, end_col=0):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_LEFT:
            if piece == 0 or piece == self.symbol:
                for i in range(col, end_col, -1):
                    board[row][i] = board[row][i - 1]
                board[row][end_col] = self.symbol

    def move_up(self, board, row, col, end_row=0):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_UP:
            if piece == 0 or piece == self.symbol:
                for i in range(row, end_row, -1):
                    board[i][col] = board[i - 1][col]
                board[end_row][col] = self.symbol

    def move_down(self, board, row, col, end_row=4):
        piece = board[row][col]
        if (row, col) in self.ALLOWED_PIECES_DOWN:
            if piece == 0 or piece == self.symbol:
                for i in range(row, end_row):
                    board[i][col] = board[i + 1][col]
                board[end_row][col] = self.symbol

    def is_winner(self, board, symbol):
        for row in board:
            if all(cell == symbol for cell in row):
                return True

        for col in range(5):
            if all(board[row][col] == symbol for row in range(5)):
                return True

        if all(board[i][i] == symbol for i in range(5)):
            return True

        if all(board[i][4 - i] == symbol for i in range(5)):
            return True

        return False

    def print_board(self, board):
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()

    def reset(self, symbol):
        self.symbol = symbol
        self.opponent_symbol = -symbol


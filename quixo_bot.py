from minimax import minimax, get_possible_moves, apply_move

class QuixoBot:
    def __init__(self, symbol):
        self.name = "QuixoBot"
        self.symbol = symbol

    def play_turn(self, board):
        best_move = None
        best_value = float('-inf') if self.symbol == 1 else float('inf')

        for move in get_possible_moves(board):
            new_board = apply_move(board, move, self.symbol)
            move_value = minimax(new_board, depth=0, is_maximizing=(self.symbol == -1), symbol=self.symbol)
            if (self.symbol == 1 and move_value > best_value) or (self.symbol == -1 and move_value < best_value):
                best_value = move_value
                best_move = move

        if best_move:
            row, col = best_move
            board[row][col] = self.symbol
        return board

    def reset(self, symbol):
        self.symbol = symbol


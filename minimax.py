
class Minimax:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def pvs(self, node, depth, alpha, beta, is_maximizing, symbol, opponent_symbol):
        if depth == 0 or node.is_terminal():
            return node.value

        if is_maximizing:
            max_eval = -float('inf')
            for child in node.children:
                eval = self.pvs(child, depth - 1, alpha, beta, False, symbol, opponent_symbol)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if alpha >= beta:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                eval = self.pvs(child, depth - 1, alpha, beta, True, symbol, opponent_symbol)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if alpha >= beta:
                    break
            return min_eval

    def search_best_move(self, root_node, bot_symbol, opponent_symbol):
        best_move = None
        best_score = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for child in root_node.children:
            score = self.pvs(child, self.max_depth, alpha, beta, False, bot_symbol, opponent_symbol)
            if score > best_score:
                best_score = score
                best_move = child.move
            alpha = max(alpha, score)
        return best_move

    def heuristic(self, board, symbol, opponent_symbol):
        my_count = 0
        opponent_count = 0
        my_potential = 0
        opponent_potential = 0

        for i in range(5):
            for j in range(5):
                cell = board[i][j]
                if cell == symbol:
                    my_count += 1
                elif cell == opponent_symbol:
                    opponent_count += 1

                if cell == 0:
                    my_potential += self.count_potential(board, i, j, symbol)
                    opponent_potential += self.count_potential(board, i, j, opponent_symbol)

        my_score = 2 * my_count + my_potential
        opponent_score = 2 * opponent_count + opponent_potential

        return my_score - opponent_score

    def count_potential(self, board, row, col, symbol):
        potential = 0
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

        for dr, dc in directions:
            line_potential = 0
            for i in range(1, 5):
                nr, nc = row + dr * i, col + dc * i
                if 0 <= nr < 5 and 0 <= nc < 5:
                    cell = board[nr][nc]
                    if cell == symbol:
                        line_potential += 1
                    elif cell != 0:
                        break
                else:
                    break
            potential += line_potential

        return potential

    def is_terminal(self, board):
        for i in range(5):
            if abs(sum(board[i])) == 5 or abs(sum(row[i] for row in board)) == 5:
                return True
        if abs(sum(board[i][i] for i in range(5))) == 5 or abs(sum(board[i][4 - i] for i in range(5))) == 5:
            return True
        return False

    def get_all_moves(self, board, symbol):
        moves = []
        for i in [0, 4]:
            for j in range(5):
                if board[i][j] == 0:
                    new_board = self.get_board_after_move(board, i, j, symbol)
                    moves.append(new_board)
        for j in [0, 4]:
            for i in range(1, 4):
                if board[i][j] == 0:
                    new_board = self.get_board_after_move(board, i, j, symbol)
                    moves.append(new_board)
        return moves

    def get_board_after_move(self, board, row, col, symbol):
        if row == 0:
            for i in range(4, 0, -1):
                board[i][col] = board[i - 1][col]
            board[0][col] = symbol
        elif row == 4:
            for i in range(4):
                board[i][col] = board[i + 1][col]
            board[4][col] = symbol
        elif col == 0:
            for j in range(4, 0, -1):
                board[row][j] = board[row][j - 1]
            board[row][0] = symbol
        elif col == 4:
            for j in range(4):
                board[row][j] = board[row][j + 1]
            board[row][4] = symbol
        return board
 
class GameNode:
    def __init__(self, board, move=None, parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.children = []
        self.value = None

    def add_child(self, child):
        self.children.append(child)

    def is_terminal(self):
        return len(self.children) == 0

    def evaluate(self, bot_symbol, opponent_symbol):
        lines = [self.board[i] for i in range(5)] + [[self.board[j][i] for j in range(5)] for i in range(5)]
        lines.append([self.board[i][i] for i in range(5)])
        lines.append([self.board[i][4 - i] for i in range(5)])
        score = 0
        for line in lines:
            score += self.evaluate_line(line, bot_symbol, opponent_symbol)
        return score

    @staticmethod
    def evaluate_line(line, bot_symbol, opponent_symbol):
        counts = {bot_symbol: 0, opponent_symbol: 0, 0: 0}
        for cell in line:
            counts[cell] += 1

        bot_count = counts[bot_symbol]
        opp_count = counts[opponent_symbol]
        empty_count = counts[0]

        if bot_count == 5:
            return 1000
        elif opp_count == 5:
            return -1000
        elif bot_count == 4 and empty_count == 1:
            return 50
        elif opp_count == 4 and empty_count == 1:
            return -50
        elif bot_count == 3 and empty_count == 2:
            return 10
        elif opp_count == 3 and empty_count == 2:
            return -10
        elif bot_count == 2 and empty_count == 3:
            return 5
        elif opp_count == 2 and empty_count == 3:
            return -5
        elif bot_count == 1 and empty_count == 4:
            return 1
        elif opp_count == 1 and empty_count == 4:
            return -1
        return 0


class GameTree:
    def __init__(self, root):
        self.root = root

    def build_tree(self, bot, depth, maximizing_player):
        self.expand_node(self.root, bot, depth, maximizing_player)

    def expand_node(self, node, bot, depth, maximizing_player):
        if depth == 0 or bot.is_winner(node.board, bot.symbol) or bot.is_winner(node.board, bot.opponent_symbol):
            node.value = node.evaluate(bot.symbol, bot.opponent_symbol)
            return
        moves = bot.generate_moves(node.board, bot.symbol if maximizing_player else bot.opponent_symbol)
        for move in moves:
            new_board = bot.apply_move(node.board, move, bot.symbol if maximizing_player else bot.opponent_symbol)
            child_node = GameNode(new_board, move, node)
            node.add_child(child_node)
            self.expand_node(child_node, bot, depth - 1, not maximizing_player)


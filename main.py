import os
from tabulate import tabulate
import time
from quixo_bot import QuixoBot
from quixo_player import Player


class QuixoGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[0] * 5 for _ in range(5)]
    
    def check_winner(self, board):
        for row in board:
            if all(cell == 1 for cell in row):
                return 1
            elif all(cell == -1 for cell in row):
                return -1
        
        for col in range(5):
            if all(row[col] == 1 for row in board):
                return 1
            elif all(row[col] == -1 for row in board):
                return -1
        
        if all(board[i][i] == 1 for i in range(5)):
            return 1
        elif all(board[i][i] == -1 for i in range(5)):
            return -1
        if all(board[i][4-i] == 1 for i in range(5)):
            return 1
        elif all(board[i][4-i] == -1 for i in range(5)):
            return -1
        
        return 0

    def play_game(self):
        turn = 0
        players = [self.player1, self.player2]
        while True:
            current_player = players[turn % 2]
            player_name = "Bot" if isinstance(current_player, QuixoBot) else "Your"
            print(f"{player_name} Turn:")
            time1 = time.time()
            self.board = current_player.play_turn(self.board)
            time2 = time.time()
            print(f"{player_name} Time taken: {time2 - time1}")
            self.print_board(self.board)
            winner = self.check_winner(self.board)
            if winner != 0:
                print(f"Player {winner} wins!")
                break
            turn += 1
    
    def print_board(self, board):
        headers = [""] + [str(i) for i in range(1, 6)]
        rows = [[str(i + 1)] + ['O' if cell == -1 else 'X' if cell == 1 else ' ' for cell in row] for i, row in enumerate(self.board)]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
        print()


os.system('cls')


if __name__ == "__main__":
    player1 = QuixoBot(1)
    player2 = Player(-1)
    game = QuixoGame(player1, player2)
    game.play_game()


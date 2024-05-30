
class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def play_turn(self, board):
        while True:
            try:
                move = input("Enter move (row col direction): ").split()
                row, col, direction = int(move[0]) - 1, int(move[1]) - 1, move[2].lower()
                if direction not in ['up', 'down', 'left', 'right']:
                    print("Invalid direction. Please choose 'up', 'down', 'left', or 'right'.")
                    continue
                if board[row][col] == 0:
                    if self.is_legal_move(row, col, direction, board):
                        board = self.update_board(row, col, direction, board)
                        return board
                    else:
                        print("Invalid move. Move is not legal.")
                else:
                    print("Invalid move. Cell is not empty.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and col as numbers between 1 and 5, and direction as 'up', 'down', 'left', or 'right'.")

    def is_legal_move(self, row, col, direction, board):
        invalid_positions = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        
        # Verificar si la casilla seleccionada tiene un borde al que se pueda mover la ficha en la dirección especificada
        if direction == 'up' and row != 0:
            return True
        elif direction == 'down' and row != 4:
            return True
        elif direction == 'left' and col != 0:
            return True
        elif direction == 'right' and col != 4:
            return True
        else:
            return False

    def update_board(self, row, col, direction, board):
        new_board = [r[:] for r in board]
        if direction == 'up':
            for i in range(4, 0, -1):
                new_board[i][col] = new_board[i-1][col]
            new_board[0][col] = self.symbol
        elif direction == 'down':
            for i in range(4):
                new_board[i][col] = new_board[i+1][col]
            new_board[4][col] = self.symbol
        elif direction == 'left':
            for j in range(4, 0, -1):
                new_board[row][j] = new_board[row][j-1]
            new_board[row][0] = self.symbol
        elif direction == 'right':
            for j in range(4):
                new_board[row][j] = new_board[row][j+1]
            new_board[row][4] = self.symbol
        return new_board

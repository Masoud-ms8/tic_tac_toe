class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            winner = self.check_winner()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True, winner
        return False, None

    def check_winner(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2] != '':
                return self.board[i][0]
            if self.board[0][i]==self.board[1][i]==self.board[2][i] != '':
                return self.board[0][i]
        if self.board[0][0]==self.board[1][1]==self.board[2][2] != '':
            return self.board[0][0]
        if self.board[0][2]==self.board[1][1]==self.board[2][0] != '':
            return self.board[0][2]
        if all(self.board[r][c] != '' for r in range(3) for c in range(3)):
            return 'Draw'
        return None

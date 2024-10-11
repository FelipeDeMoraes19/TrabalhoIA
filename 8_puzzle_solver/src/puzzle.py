import copy


class PuzzleState:
    def __init__(self, board, empty_pos, parent=None, move=None):
        self.board = board
        self.empty_pos = empty_pos
        self.parent = parent
        self.move = move
    
    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def possible_moves(self):
        moves = []
        x, y = self.empty_pos
        if x > 0:
            moves.append("up")
        if x < 2:
            moves.append("down")
        if y > 0:
            moves.append("left")
        if y < 2:
            moves.append("right")
        return moves
    
    def apply_move(self, move):
        new_board = copy.deepcopy(self.board)
        x, y = self.empty_pos
        if move == "up":
            new_board[x][y], new_board[x-1][y] = new_board[x-1][y], new_board[x][y]
            new_empty_pos = (x-1, y)
        elif move == "down":
            new_board[x][y], new_board[x+1][y] = new_board[x+1][y], new_board[x][y]
            new_empty_pos = (x+1, y)
        elif move == "left":
            new_board[x][y], new_board[x][y-1] = new_board[x][y-1], new_board[x][y]
            new_empty_pos = (x, y-1)
        elif move == "right":
            new_board[x][y], new_board[x][y+1] = new_board[x][y+1], new_board[x][y]
            new_empty_pos = (x, y+1)
        return PuzzleState(new_board, new_empty_pos, parent=self, move=move)

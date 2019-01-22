# col, row
WHITE = 1
BLACK = 2
one = [[None, None, None, None, None, None],
       [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), None],
       [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), None],
       [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), None],
       [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), None],
       [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), None],
       [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10)],
       [(6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9)],
       [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
       [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)],
       [(9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)]]

two = [[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
       [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)],
       [(3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
       [(4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9)],
       [(5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10)],
       [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), None],
       [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), None],
       [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), None],
       [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), None],
       [(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), None],
       [None, None, None, None, None, None]]

three = [[(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
         [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6)],
         [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)],
         [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8)],
         [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)],
         [None, (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9)],
         [None, (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8)],
         [None, (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)],
         [None, (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)],
         [None, (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5)],
         [None, None, None, None, None, None]]

four = [[None, None, None, None, None, None],
        [None, (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)],
        [None, (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6)],
        [None, (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)],
        [None, (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8)],
        [None, (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9)],
        [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9)],
        [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8)],
        [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)],
        [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6)],
        [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5)]]

field =  [[None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None, None],
          [None, None, None, None, None, None, None],
          [None, None, None, None, None, None]]

def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE
 
color = WHITE
if color == BLACK:
    do_something()
color == other_color
opponent_color = opponent(color)

class Board:
    def __init__(self):
        self.color = WHITE
        self.field =  [[None, None, None, None, None, None],
                       [None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None, None],
                       [None, None, None, None, None, None, None],
                       [None, None, None, None, None, None]]
    def correct_coords(col, row):
        if row >= 0 and col >= 0 and col < 11 and row < len(field[col]):
            return True
        return False
    def current_player_color(self):
        return self.color
 
    def cell(self, col, row):
        piece = self.field[col][row]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()
 
    def move_piece(self, col, row, col1, row1):
 
        if not correct_coords(col, row) or not correct_coords(col1, row1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[col][row]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[col1][row1] is None:
            if not piece.can_move(self, col, row, col1, row1):
                return False
        elif self.field[col1][row1].get_color() == opponent(piece.get_color()):
            if not piece.can_eat(self, col, row, col1, row1):
                return False
        else:
            return False
        if piece.check_Q:
            self.field[col1][row1] = Queen(piece.col, piece.row, piece.color)
        else:
            self.field[col1][row1] = piece
        self.field[col][row] = None
        self.color = opponent(self.color)
        return True

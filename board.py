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

Pieces = [[Pawn(1, 0, 1, 0), Pawn(2, 1, 1, 1), Pawn(3, 2, 1, 2), Pawn(4, 3, 1, 3),
           Pawn(5, 4, 1, 4), Pawn(6, 3, 1, 5), Pawn(7, 2, 1, 6), Pawn(8, 1, 1, 7),
           Pawn(9, 0, 1, 8), King(6, 0, 1, 9), Queen(4, 0, 1, 10), Rook(2, 0, 1, 11),
           Rook(8, 0, 1, 12), Knight(3, 0, 1, 13), Knight(7, 0, 1, 14), Bishop(5, 0, 1, 15),
           Bishop(5, 1, 1, 16), Bishop(5, 2, 1, 17)],
          [Pawn(1, 6, 2, 0), Pawn(2, 6, 2, 1), Pawn(3, 6, 2, 2), Pawn(4, 6, 2, 3),
           Pawn(5, 6, 2, 4), Pawn(6, 6, 2, 5), Pawn(7, 6, 2, 6), Pawn(8, 6, 2, 7),
           Pawn(9, 6, 2, 8), King(6, 9, 2, 9), Queen(4, 9, 2, 10), Rook(2, 7, 2, 11),
           Rook(8, 7, 2, 12), Knight(3, 8, 2, 13), Knight(7, 8, 2, 14), Bishop(5, 10, 2, 15),
           Bishop(5, 9, 2, 16), Bishop(5, 8, 2, 17)]]
           

def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE

def print_board():
        a = ''
        b = []
        for i in field:
            q = []
            for j in i:
                if j == None:
                    b.append('  ')
                else:
                    q.append(j[1])
            b.append('\t'.join(q))
        a = '\n'.join(b)
        print(a)

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
        field = self.field
        
    def correct_coords(col, row):
        if row >= 0 and col >= 0 and col < 11 and row < len(field[col]):
            return True
        return False
    
    def current_player_color(self):
        return self.color
 
    def out(self, col, row):
        obj = self.field[col][row][0]
        if obj[0] is None:
            return None
        piece = Pieces[obj[0]][obj[1]]
        return piece.char()[1]
 
    def move_piece(self, col, row, col1, row1):
        if not correct_coords(col, row) or not correct_coords(col1, row1):
            return False
        if row == row1 and col == col1:
            return False
        obj = self.field[col][row][0]
        if obj[0] is None:
            return False
        piece = Pieces[obj[0]][obj[1]]
        if piece.get_color() != self.color:
            return False
        if self.field[col1][row1][0] is None:
            if not piece.can_move(self, col, row, col1, row1):
                return False
        else:
            obj1 = self.field[col1][row1][0]
            piece1 = Pieces[obj1[0]][obj1[1]]            
            if piece1.get_color() == opponent(piece.get_color()):
                if not piece.can_eat(self, col, row, col1, row1):
                    return False
                else:
                    Pieces[obj[0]][obj[1]] = None
            else:
                return False
        piece.col = col1
        piece.row = row1
        self.field[col][row] = None
        self.field[col1][row1] = piece.char()
        self.color = opponent(self.color)
        if piece.check_Q:
            Pieces[obj[0]][obj[1]] = Queen(piece.col, piece.row, piece.color, piece.N)
            self.field[col1][row1] = Pieces[obj[0]][obj[1]].char()
        field = self.field
        return True
    
    def start(self):
        for i in range(len(Pieces)):
            for j in range(len(Pieces[i])):
                piece = Pieces[i][j]
                char = piece.char()
                self.field[char[2][0]][char[2][1]] = char
        field = self.field

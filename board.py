WHITE = 1
BLACK = 2
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
# row - стока col - столбец
# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE
 
# Инициализация цвета
color = WHITE
# Проверка цвета
if color == BLACK:
    do_something()
# сравнение цветов
color == other_color
# Цвет противника
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
    def correct_coords(row, col):
        if row >= 0 and col >= 0 and col < 11 and row < len(field[col]):
            return True
        return False
    def current_player_color(self):
        return self.color
 
    def cell(self, row, col):
        '''Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела.'''
        piece = self.field[col][row]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()
 
    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''
 
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[col][row]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[col1][row1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[col1][row1].get_color() == opponent(piece.get_color()):
            if not piece.can_eat(self, row, col, row1, col1):
                return False
        else:
            return False
        if piece.check_Q:
            self.field[col1][row1] = Queen(piece.row, piece.col, piece.color)
        else:
            self.field[col1][row1] = piece
        self.field[col][row] = None
        self.color = opponent(self.color)
        return True
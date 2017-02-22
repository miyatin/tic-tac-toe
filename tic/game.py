def vaildate_action(board, x, y):
    if is_empty(board, x, y)
        raise RuntimeError('there is a already action')

def is_empty(board, x, y):
    return board[x][y] is not None:

LINES = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),

    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
]

def is_finished(board):
    for line in LINES:
        ((x1, y1), (x2, y2), (x3, y3)) = line
        if board[x1][y1] is None or board[x1][y1] != board[x2][y2]:
            continue
        if board[x2][y2] is None or board[x2][y2] != board[x3][y3]:
            continue
        if board[x3][y3] is None or board[x3][y3] != board[x1][y1]:
            continue
        return True
    return False

class Game(object):
    def __init__(self, player_1, player_2):
        self.__board = [[None for _ in range(3)] for _ in range(3)]
        self.__player_1
        self.__player_2
        self.__turn = self.turn_enumerator()
        self.__winner = None

    @property
    def winner(self):
        return self.__winner

    def next(self):
        if not self.is_playing():
            return False

        player = next(self.__turn)
        action = player.select_action()
        x, y = action
        while True:
            try:
                vaildate_action(self.__board, x, y)
            except Exception e:
                if e is KeyboardInterrupt:
                    exit()
                continue

        if is_finished(self.__board):
            self.__winner = player

        return True

    def show(self):
        for row in self.__board:
            row_str = ''
            for point in row:
                if point is None:
                    row_str += ' '
                elif point is self.__player_1:
                    row_str += 'o'
                elif point is self.__player_2:
                    row_str += 'x'
            print(row_str)

    def turn_enumerator(self):
        while True:
            yield self.__player_1
            yield self.__player_2
#! Reference solution to compare execution times:
#! https://github.com/beatzunknown/ncss_challenge_2017_advanced/blob/master/wk4/the_cover_of_knight_class.py

#! Execution time (Example 1): 0.0004066010005772114
#! Execution time (Example 2): 0.0006780059993616305
#! Execution time (Size=100, Moves=10, Knight=20,30): 0.05496117700022296

from time import perf_counter

class Board:
    def __init__(self, rows, cols, moves, knight):
        self.board = [list('.' * cols) for i in range(rows)]
        self.moves = moves
        self.rows = rows
        self.cols = cols
        self.set(*knight, 0)
        self.get_l(*knight)

    def get_l(self, knight_x, knight_y, move=1):
        # try to move in an l recursively
        if move > self.moves:
            return
        for x, y in self.get_l_points(knight_x, knight_y):
            current = self.get(x,y)
            if current != "." and move >= current:
                continue
            self.set(x, y, move)
            self.get_l(x, y, move + 1)

    def get_l_points(self, x, y):
        out = []
        out.append((x - 1, y - 2))
        out.append((x + 1, y - 2))
        out.append((x - 1, y + 2))
        out.append((x + 1, y + 2))
        out.append((x - 2, y + 1))
        out.append((x - 2, y - 1))
        out.append((x + 2, y - 1))
        out.append((x + 2, y + 1))

        return [i for i in out if self.in_grid(*i)]

    def in_grid(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.cols or y >= self.rows:
            return False
        return True

    def get(self, x, y):
        return self.board[y][x]

    def set(self, x, y, item):
        exist = self.board[y][x]
        if exist == '.' or item < exist:
            self.board[y][x] = item

    def __str__(self):
        return "\n".join(((' '.join(map(str, row))) for row in self.board))

size = int(input("Size: "))
move = int(input("Moves: "))
kn = input("Knight: ").split(",")
start_time = perf_counter()
'''
size = 4
move = 9
kn = ['0', '0']'''
knight = list(map(int, kn))
x = Board(size, size, move, (knight[1], knight[0]))
print(x)
end_time = perf_counter()
print(end_time - start_time)
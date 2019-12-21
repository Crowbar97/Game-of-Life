from random import randrange
from patterns import patterns

# TODO: add ability to spawn patterns in runtime
# in the specified place
# TODO: add game end tracking
# and corresponding actions
# (e.g. spawning and explosions)
class Biome:
    def __init__(self, row_count, col_count, live_cell_count):
        self.live_cell = "\u25CF"
        self.dead_cell = "x"

        self.row_count = row_count
        self.col_count = col_count

        self.field = self.make_field()
        self.init_field(live_cell_count)

    def make_field(self):
        field = []
        for _ in range(self.row_count):
            field.append([])
            for _ in range(self.col_count):
                field[-1].append(self.dead_cell)
        return field

    def is_alive(self, cell):
        return cell == self.live_cell

    def make_live(self, cells, field=None):
        if field == None:
            field = self.field
        for (i, j) in cells:
            field[i][j] = self.live_cell

    def init_field(self, cell_count):
        while cell_count > 0:
            i = randrange(self.row_count)
            j = randrange(self.col_count)
            if not self.is_alive(self.field[i][j]):
                self.make_live([(i, j)])
                cell_count -= 1

    def print_fence(self):
        print("+", end="")
        for _ in range(self.col_count):
            print("-", end="")
        print("+")

    def print_field(self):
        self.print_fence()
        for row in self.field:
            print("|", end="")
            for cell in row:
                if self.is_alive(cell):
                    print('\033[32m', cell, '\033[0m', sep="", end="")
                else:
                    print('\033[90m', cell, '\033[0m', sep="", end="")
            print("|")
        self.print_fence()

    def nb_count(self, i0, j0):
        nb_count = 0
        for i in range(i0 - 1, i0 + 2):
            for j in range(j0 - 1, j0 + 2):
                if 0 <= i < self.row_count and 0 <= j < self.col_count:
                    nb_count += self.is_alive(self.field[i][j])
        nb_count -= self.is_alive(self.field[i0][j0])
        return nb_count

    def next(self):
        new_field = self.make_field()
        for i in range(self.row_count):
            for j in range(self.col_count):
                nb_count = self.nb_count(i, j)
                if self.is_alive(self.field[i][j]):
                    if 2 <= nb_count <= 3:
                        self.make_live([(i, j)], new_field)
                else:
                    if nb_count == 3:
                        self.make_live([(i, j)], new_field)
        self.field = new_field

    # FIXME: out of range
    def make_pattern(self, name, i0, j0):
        self.make_live(map(lambda pos:
                                (pos[0] + i0, pos[1] + j0),
                           patterns[name]))


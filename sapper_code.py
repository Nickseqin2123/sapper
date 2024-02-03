from random import sample


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        return cls.__instance

    def __init__(self, n, m, total_mines):
        self.__pole_cells = [[Cell() for i in range(m)] for j in range(n)]
        self.total_mines = total_mines
        self.n = n
        self.m = m

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines_counter = 0
        ser = []
        for i in range(self.n):
            for j in range(self.m):
                ser.append(self.pole[i][j])
        a = sample(ser, self.total_mines)
        for i in a:
            i.is_mine = True
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for xx in range(self.n):
            for y in range(self.m):
                if not self.pole[xx][y].is_mine:
                    mines = sum((self.pole[xx + i][y + j].is_mine for i,j in indx if 0 <= xx + i < self.n and 0 <= y + j < self.m))
                    self.pole[xx][y].number = mines

    def open_cell(self, i, j):
        if i > self.n - 1 or j > self.m:
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.pole[i][j].is_open = True

    def show_pole(self):
        for i in range(self.n):
            for j in range(self.m):
                print("💣" if self.pole[i][j].is_mine else "🌕", end="")
            print()


class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = None
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, val):
        if isinstance(val, bool) is False:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = val

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, val):
        if (0 <= val < 8) is False:
            raise ValueError("недопустимое значение атрибута")
        self.__number = val

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, val):
        if isinstance(val, bool) is False:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = val

    def __bool__(self):
        if self.__is_open is True:
            return False
        return True

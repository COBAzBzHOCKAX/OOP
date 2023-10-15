from dot import *

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow # Точка, где размещён нос корабля
        self.l = l # длина корабля
        self.o = o # Направление корабля (0 - вертикальное, 1 - горизонтальное)
        self.lives = l # Количеством жизней (сколько точек корабля еще не подбито)

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots
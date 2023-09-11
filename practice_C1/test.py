class Game:

    field_size = 6
    count_ship = [0, #всегда нулевое значение
                  4, #сколько кораблей с 1 палубой
                  2, #сколько кораблей с 2 палубами
                  1, #сколько кораблей с 3 палубами
                  0] #сколько кораблей с 4 палубами

class Ship(Game):

    """
    Данный класс используется для хранения информации о корабле, такой как начальные координаты корабля,
    горизонтальная или вертикальная ориентация на поле, его статус (живой, подбитый, мёртвый), размеры.
    ---------------------------------------------------------------------------------------------------

    Класс поддерживает следующие методы:

    self.position - может как принимать, так и возвращать информацию о позиции корабля на поле. Чтобы ввести координаты
    корабля, введите self.position(x, y)

    self.is_alive - может как принимать, так и возвращать информацию о статусе корабля
    (2 - живой, 1 - подбит, 0 - мертвый)

    self.
    """

    def __init__(self) -> None:
        self.__x = None # начальная точка x
        self.__y = None # начальная точка x
        self.__orient = 0 # 0 - горизонтальное ориентирование корабля на поле, 1 - вертикальное
        self.__is_alive = 1 # статус корабля, живой (2), подбит (1), убит (0)
        self.__size = None # размеры корабля

    @property
    def position(self):
        return (self.__x, self.__y)

    @position.setter
    def position(self, x, y):
        if 1 <= x <= super().field_size and 1<= y <= super().field_size:
            self.__x = x
            self.__y = y
        else:
            raise ValueError(f'Координаты x={x}, y={y} выходят за рамки поля {super().field_size}x{super().field_size}')


    @property
    def is_alive(self):
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, is_alive):
        if 0 <= is_alive <= 2:
            self.__is_alive = is_alive
        else:
            raise ValueError(f'''
            Значение для метода {self.is_alive.__qualname__} не может принимать значение {is_alive}.
            Данный метод описывает состояние корабля цифрами от 0 до 2, где:
                2 - живой
                1 - подбит
                0 - убит
                              ''')

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        for i in Game.count_ship:
            if i ==
                self.__size = size
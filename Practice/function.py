class Area:

    __PI = 3.14

    def circle_area(self, r):
        return self.__PI * (r ** 2)


    def rect_area(self, a, b):
        return a * b


if __name__ == '__main__':
    # проверяем работоспособность функции, дальнейшая часть не будет импортирована
    assert Area.circle_area(5) == 78.5  # если ответы будут отличаться, то будет вызвана ошибка
    assert Area.rect_area(5, 4) == 20
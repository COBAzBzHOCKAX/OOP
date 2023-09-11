from rectangle import Rectangle, Square, Circle

# создаём два прямоугольника

rect_1 = Rectangle(3, 4, 15, 23)
rect_2 = Rectangle(12, 5, 43, 12)
#вывод площади двух прямоугольников
print(rect_1.get_area())
print(rect_2.get_area())
print(rect_1 == rect_2)
print(rect_1)

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())
print(square_1 == square_2)

circle_1 = Circle(6)
circle_2 = Circle(12)

print(circle_1.get_area_circle(),
      circle_2.get_area_circle())

print()
figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance (figure, Square):
        print(figure.get_area_square())
    elif isinstance (figure, Circle):
        print(figure.get_area_circle())
    else:
        print(figure.get_area())
    print()
print()

print()
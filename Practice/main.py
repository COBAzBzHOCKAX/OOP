from factory import create_app

S = create_app

s_circle = S.circle_area(int(input('Введите радиус круга: ')))
print('Введите размеры сторон квадрата')
s_rect = S.rect_area(int(input('a = ')), int(input('b = ')))

if s_circle > s_rect:
    print('Площадь круга больше квадрата')
elif s_circle < s_rect:
    print('Площадь квадрата больше круга')
else:
    print('Площади фигур равны')
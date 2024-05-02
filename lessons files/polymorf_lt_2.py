# Задача №2 с использованием полиморфизма.
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape(object):
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Square (Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

def print_area(shape):
    print(f'Площадь фигуры: {shape.area()}')


circle = Circle(5)
print_area(circle)

square = Square(5)
print_area(square)
#Создайте класс Animal с методом make_sound(). Затем создайте несколько дочерних классов (например, Dog, Cat, Cow),
# которые наследуют Animal, но изменяют его поведение (метод make_sound()). В конце создайте список содержащий
# экземпляры этих животных и вызовите make_sound() для каждого животного в цикле.

class Animal():
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print('Гав')

class Cat(Animal):
    def make_sound(self):
        print('Мяу')

class Cow(Animal):
    def make_sound(self):
        print('Мууу')

animals = [Dog(), Cat(), Cow()]
for animal in animals:
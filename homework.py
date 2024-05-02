# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите
# методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и
# сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age, voice):
        self.name = name
        self.age = age
        self.voice = voice

    def make_sound(self):
        print(f'{self.name} издает звук - {self.voice}')

    def eat(self):
        print(f'{self.name} ест')

class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age, voice)
        self.color = color


class Mammal(Animal):
    def __init__(self, name, age, type, voice):
        super().__init__(name, age, voice)
        self.type = type

class Reptile(Animal):
    def __init__(self, name, age, voice):
        super().__init__(name, age, voice)

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк')

    def add_staff(self, staff, name):
        self.name = name
        self.staff.append(staff)
        print(f'Сотрудник {self.name} добавлен в зоопарк')

class ZooKeeper(Zoo):
    def feed_animal(self, animal):
        print(f'Животное {animal.name} покормлено')
class Veterinarian(Zoo):
    def heal_animal(self, animal):
        print(f'Животное {animal.name} вылечено')



reptile1 = Reptile('варан', 1, 'чщщщ')
bird1 = Bird('попугай', 2, 'красный', 'кря-кря')
bird2 = Bird('голубь', 4, 'синий', 'курлык')
mammal1 = Mammal('тигр', 5, 'хищник', 'рррррр')
mammal2 = Mammal('лошадь', 7, 'травоядный', 'игого')

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(reptile1)
zoo.add_animal(bird1)
zoo.add_animal(bird2)
zoo.add_animal(mammal1)
zoo.add_animal(mammal2)

zoo.add_staff(keeper, 'Петя')
zoo.add_staff(veterinarian, 'Вася')

animal_sound(zoo.animals)

keeper.feed_animal(mammal1)

veterinarian.heal_animal(bird1)
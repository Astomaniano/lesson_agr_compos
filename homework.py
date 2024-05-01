# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите
# методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и
# сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и
# `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} издает звук - {self.voice}')

    def eat(self):
        print(f'{self.name} ест')

class Bird(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.color = color
        self.voice = voice


class Mammal(Animal):
    def __init__(self, name, age, type, voice):
        super().__init__(name, age)
        self.type = type
        self.voice = voice

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.voice = voice



bird1 = Bird('попугай', 2, 'красный', 'кря-кря')
bird2 = Bird('голубь', 4, 'синий', 'курлык')
mammal1 = Mammal('тигр', 5, 'хищник', 'рррррр')
mammal2 = Mammal('лошадь', 7, 'травоядный', 'игого')

mammal1.make_sound()

class Dog:
    def speak(self):
        print('Гав')

class Cat:
    def speak(self):
        print('Мяу')

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)
animal_speak(cat)
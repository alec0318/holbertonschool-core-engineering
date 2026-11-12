#!/us/bin/env python3
class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

dog = Dog()
cat = Cat()

animals = [Dog(), Cat(), Dog()]
for animal in animals:
    print(animal.speak())

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
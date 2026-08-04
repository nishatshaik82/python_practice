class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Bow Bow")


class Cat(Animal):
    def sound(self):
        print("Meow Meow")


class Cow(Animal):
    def sound(self):
        print("Moo Moo")


# Main program
dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
cat.sound()
cow.sound()
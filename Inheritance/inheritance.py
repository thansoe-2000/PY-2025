# inheritance
class Animal:
    def eat(self):
        print("I can eat.")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

d = Dog() # object တစ်ခု ဆောက်ထား
d.eat()
d.bark()

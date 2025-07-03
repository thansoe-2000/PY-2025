#  class Attribute
#  Class Attribute ဆိုတာက class level မှာ သတ်မှတ်ထားတဲ့ attribute
#  Object (instance) တစ်ခုချင်းစီမှာ မဟုတ်ဘဲ class ကိုပိုင်တဲ့ attribute ဖြစ်တယ်။


class Dog:
    species ="Canine" # <----- class Attribute

    def __init__(self, name):
        self.name = name # <-----instance attribute
d1 = Dog("Bobby")
d2 = Dog("Lucky")

print(d1.species)
print(d2.species)
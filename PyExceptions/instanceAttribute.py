# instance attribute
class Person:
    def __init__(self, name, age):
        self.name = name # instance attribute
        self.age = age # instance attribute

p1 = Person("Than Soe", 24)
p2 = Person("Aung Aung", 22)

print(p1.name)
print(p2.name)
print(type(p1))
print(hasattr(p1, 'age'))

# p1 and p2 are objects,
# they are created as object using Person() class
# Person is class
# p1 and p2 ထဲမှာ name, age ဆိုရေ Attribute တိ ပါရေ
# object တစ်ခုချင်းစီမှာ မတူရေ data တိကို store လုပ် ဖို့ သုံးရေ။
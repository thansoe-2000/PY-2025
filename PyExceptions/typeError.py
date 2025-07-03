# pytho type error

a = 5
b = "Hello"
print(a + b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


def add(x, y):
    return x + y
add("hello", 5)
# TypeError: can only concatenate str (not "int") to str
# Wrong data type used
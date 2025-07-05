# assert condition, "Optional error message"

x = 5
assert x > 0, " x must be positive"
print("x is positive")

def divide(a, b):
    assert b != 0
    return a / b

print(divide(10, 2))
print(divide(5, 0))
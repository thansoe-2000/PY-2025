# IndexError ဆိုတာ Python မှာ list (သို့) array တစ်ခုရဲ့ မရှိတဲ့
#  index ကို access လုပ်ချင်တဲ့အခါ ဖြစ်တယ်။


# valid
# my_list = [10, 20, 30]
# print(my_list[2])

# my_list = [10, 20, 30]
# print(my_list[5])
# IndexError: list index out of range
# မဟိေရ Index ကို ရှာလို့ ဖြစ်တေ error

# text = "hello"
# print(text[10])
# IndexError: string index out of range

# t = (1, 2, 3)
# print(t[4])
# IndexError: tuple index out of range

# my_list = [10, 20, 30, 40]
# if len(my_list) > 3:
#     print(my_list[2])


my_list = [10, 20, 30, 40]

try:
    print(my_list[5])
except IndexError:
    print("Index out of bound")

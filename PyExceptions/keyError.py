# keyError
# my_dict = {"name": "Than Soe", "age":24}
# print(my_dict["address"])
# # KeyError: 'address'

# data = {"a":1, "b":2}
# data.pop("c")
# # KeyError: 'c'


# my_dict = {"name": "Than Soe", "age":24}
# if "address" in my_dict:
#     print(my_dict["address"])
# else:
#     print("Address not found.")

my_dict = {"name": "Than Soe", "age":24, "address":"Ponnagyun"}
try:
    print(my_dict["address"])
except KeyError:
    print("Key doesn't exit.")

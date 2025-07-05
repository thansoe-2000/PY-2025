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

# my_dict = {"name": "Than Soe", "age":24, "address":"Ponnagyun"}
# try:
#     print(my_dict["name"])
# except KeyError:
#     print("Key doesn't exit.")


students = {
    "s001":"Aung Soe",
    "s002":"Aung Min",
    "s003":"Aung Paing",
    "s003":"Aung Than Soe",
}
print(students.get("s003"))
# student_id = input("Enter student ID: ")

# try:
#     name = students[student_id]
#     print(f"Student name: {name}")
# except KeyError:
#     print("Student ID not found!")

if "s001" in students:
    print(students["s001"])
else:
    print("No such key!")

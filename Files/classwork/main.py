# with open("Files/classwork/1.txt", "w") as file:
#     file.write("Hello")



# with open("Files/classwork/1.txt") as file:
#     text = file.read()

# print(text)


import json




with open("Files/classwork/users.json", "r") as file:
    users = json.load(file)

print(users)
users.update(
    {
        "Hanna": 10
    }
)


with open("Files/classwork/users.json", "w") as file:
    json.dump(users, file)

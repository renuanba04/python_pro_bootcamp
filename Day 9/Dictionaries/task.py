programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary)
# add new item
programming_dictionary["Loop"] = "A piece of code that runs over and over again."

print(f"After adding new item: {programming_dictionary}")

# edit an item
programming_dictionary["Bug"] = "It hinders program execution"

print(f"After editing an item: {programming_dictionary}")

# print each key separately
for key in programming_dictionary:
    print(f"Key: {key}")

# print each value
for key in programming_dictionary:
    print(f"Value: {programming_dictionary[key]}")




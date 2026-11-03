enemies = 1


def increase_enemies():
    enemies = 2 # local scope - variable has been shadowed
    print(f"enemies inside function: {enemies}")


increase_enemies()
# end of function call the local scope variables lose their name and value
print(f"enemies outside function: {enemies}") # referencing the global scope variable in line 1

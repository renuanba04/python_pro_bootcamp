import random

# other random functions
print("\nRange: 0.0 <= N < 1.0")
for _ in range(10):
    # prints float number between 0.0 <= N < 1.0
    rand_float = random.random()
    print(rand_float)

print("\nRange: 0.0 <= N < 10.0")
for _ in range(10):
    # prints float number between 0.0 <= N < 10.0
    rand_float_larger_range = random.random() * 10
    print(rand_float_larger_range)

print("\nRange: 0.0 <= N <= 5.0")
for _ in range(10):
    # prints float number between 0.0 <= N <= 5.0
    rand_float_larger_range = random.uniform(0,5)
    print(rand_float_larger_range)

# creating our own module
import my_module
print("\nAccessing custom module")
print(f"my_module.my_favorite_number = {my_module.my_favorite_number}")

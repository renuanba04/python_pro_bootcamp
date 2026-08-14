import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
bill_payer = random.randint(0,4)
print(friends[bill_payer])

# Option 2
print(random.choice(friends))
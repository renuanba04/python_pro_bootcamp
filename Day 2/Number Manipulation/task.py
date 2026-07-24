bmi = 84 / 1.65 ** 2

# float
print(bmi)

# int
print(int(bmi))

# round
print(round(bmi))
print(round(bmi, 2))

# assignment operators
score = 132
print(score)
score += 35
print(score)
score -= 57
print(score)
score *= 2
print(score)
score //= 15
print(score)
score %= 3
print(score)
score **= 4
print(score)
score /= 5
print(score)

# without f strings
print("Score:" + str(score))
# f strings
print(f"Score:{score}")
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)
print(f"Total Score using sum(): {total_score}")

# using for loops
total = 0
for score in student_scores:
    total += score

print(f"Total score using for loop: {total}")

max_score = max(student_scores)
print(f"Maximum score using max(): {max_score}")

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(f"Maximum score using for loops: {max_score}")

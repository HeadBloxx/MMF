student_scores = [150, 142, 185, 128, 171, 184, 149, 24, 59, 68, 199, 78, 65]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest = 0
for h_score in student_scores:
    if h_score > highest:
        highest = h_score

print(f"The highest score in the class is: {highest} ")
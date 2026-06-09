students = [
    {"name": "Alice", "subject": "Maths", "scores": [85, 92, 78, 90]},
    {"name": "Bob", "subject": "Science", "scores": [45, 52, 38, 41]},
    {"name": "Carol", "subject": "Maths", "scores": [72, 68, 75, 80]},
    {"name": "David", "subject": "English", "scores": [55, 60, 58, 62]},
    {"name": "Eve", "subject": "Science", "scores": [90, 95, 88, 92]},
    {"name": "Frank", "subject": "English", "scores": [30, 25, 40, 35]},
    {"name": "Grace", "subject": "Maths", "scores": [65, 70, 68, 72]},
    {"name": "Heidi", "subject": "Science", "scores": [48, 45, 50, 47]},
    {"name": "Ivan", "subject": "English", "scores": [88, 92, 85, 90]},
    {"name": "Judy", "subject": "Maths", "scores": []}
]

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

# Calculate average score for each student
student_averages = {student["name"]: calculate_average(student["scores"]) for student in students}

# Find the highest and lowest scoring students overall
overall_scores = [(student["name"], calculate_average(student["scores"])) for student in students]
highest_scoring_student, highest_score = max(overall_scores, key=lambda x: x[1])
lowest_scoring_student, lowest_score = min(overall_scores, key=lambda x: x[1])

# Group students by subject and calculate average score per subject
subject_averages = {}
for student in students:
    subject = student["subject"]
    scores = student["scores"]
    if subject not in subject_averages:
        subject_averages[subject] = []
    subject_averages[subject].extend(scores)

for subject, scores in subject_averages.items():
    subject_averages[subject] = calculate_average(scores)

# Identify failing students (average below 50)
failing_students = [name for name, average in student_averages.items() if average < 50]

# Print formatted report
print("Student Averages:")
for name, average in student_averages.items():
    print(f"{name}: {average:.2f}")

print("\nHighest Scoring Student Overall:")
print(f"{highest_scoring_student}: {highest_score:.2f}")

print("\nLowest Scoring Student Overall:")
print(f"{lowest_scoring_student}: {lowest_score:.2f}")

print("\nAverage Score per Subject:")
for subject, average in subject_averages.items():
    print(f"{subject}: {average:.2f}")

print("\nFailing Students (Average Below 50):")
if failing_students:
    for name in failing_students:
        print(name)
else:
    print("No students are failing.")

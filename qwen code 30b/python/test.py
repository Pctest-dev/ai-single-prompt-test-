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
    """Calculate average of scores, handling empty list case."""
    if not scores:
        return 0
    return sum(scores) / len(scores)

# Calculate average score for each student
for student in students:
    student["average"] = calculate_average(student["scores"])

# Find highest and lowest scoring student overall
highest_scoring_student = max(students, key=lambda x: x["average"])
lowest_scoring_student = min(students, key=lambda x: x["average"])

# Group students by subject and calculate average score per subject
subject_averages = {}
for student in students:
    subject = student["subject"]
    if subject not in subject_averages:
        subject_averages[subject] = []
    subject_averages[subject].append(student["average"])

# Calculate final averages for each subject
final_subject_averages = {subject: sum(averages)/len(averages) 
                         for subject, averages in subject_averages.items()}

# Identify failing students (average below 50)
failing_students = [student for student in students if student["average"] < 50]

# Print formatted report
print("=" * 60)
print("STUDENT ACADEMIC REPORT")
print("=" * 60)

print(f"\nHighest Scoring Student: {highest_scoring_student['name']} "
      f"({highest_scoring_student['average']:.2f})")

print(f"Lowest Scoring Student: {lowest_scoring_student['name']} "
      f"({lowest_scoring_student['average']:.2f})")

print("\nSubject Averages:")
for subject, average in final_subject_averages.items():
    print(f"  {subject}: {average:.2f}")

print("\nFailing Students (Average < 50):")
if failing_students:
    for student in failing_students:
        print(f"  {student['name']}: {student['average']:.2f}")
else:
    print("  None")

print("\nAll Student Averages:")
for student in students:
    print(f"  {student['name']}: {student['average']:.2f}")

print("=" * 60)

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
    """Calculate average of scores, return 0 for empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# Calculate average for each student
student_averages = []
for student in students:
    avg = calculate_average(student["scores"])
    student_averages.append({
        "name": student["name"],
        "subject": student["subject"],
        "average": avg,
        "scores": student["scores"]
    })

# Find highest and lowest scoring students overall
if student_averages:
    highest_student = max(student_averages, key=lambda x: x["average"])
    lowest_student = min(student_averages, key=lambda x: x["average"])
else:
    highest_student = lowest_student = None

# Group by subject and calculate subject averages
from collections import defaultdict

subject_scores = defaultdict(list)
for student in students:
    subject_scores[student["subject"]].extend(student["scores"])

subject_averages = {}
for subject, scores in subject_scores.items():
    if scores:
        subject_averages[subject] = sum(scores) / len(scores)
    else:
        subject_averages[subject] = 0.0

# Identify failing students
failing_students = [s for s in student_averages if s["average"] < 50]

# Print formatted report
print("=" * 60)
print("STUDENT PERFORMANCE REPORT")
print("=" * 60)

print("\nIndividual Student Results:")
print("-" * 40)
for s in student_averages:
    status = "FAIL" if s["average"] < 50 else "PASS"
    scores_str = ", ".join(map(str, s["scores"])) if s["scores"] else "NO SCORES"
    print(f"{s['name']:8} | {s['subject']:8} | Avg: {s['average']:6.2f} | {status} | Scores: {scores_str}")

print("\nOverall Top and Bottom Performers:")
print("-" * 40)
if highest_student:
    print(f"Highest scorer : {highest_student['name']} ({highest_student['subject']}) - {highest_student['average']:.2f}")
if lowest_student:
    print(f"Lowest scorer  : {lowest_student['name']} ({lowest_student['subject']}) - {lowest_student['average']:.2f}")

print("\nSubject-wise Average Performance:")
print("-" * 40)
for subject in sorted(subject_averages.keys()):
    print(f"{subject:10} : {subject_averages[subject]:.2f}")

print("\nFailing Students (Average < 50):")
print("-" * 40)
if failing_students:
    for s in failing_students:
        print(f"• {s['name']} ({s['subject']}) - Average: {s['average']:.2f}")
else:
    print("No students are failing.")

print("\n" + "=" * 60)
print("End of Report")
print("=" * 60)
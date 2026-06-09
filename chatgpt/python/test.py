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
    """Return the average score or None if no scores exist."""
    if not scores:
        return None
    return sum(scores) / len(scores)


# Calculate student averages
student_averages = []

for student in students:
    avg = calculate_average(student["scores"])

    student_averages.append({
        "name": student["name"],
        "subject": student["subject"],
        "average": avg
    })

# Find highest and lowest scoring students
valid_students = [s for s in student_averages if s["average"] is not None]

highest_student = max(valid_students, key=lambda s: s["average"]) if valid_students else None
lowest_student = min(valid_students, key=lambda s: s["average"]) if valid_students else None

# Group by subject
subject_data = {}

for student in students:
    subject = student["subject"]
    avg = calculate_average(student["scores"])

    if subject not in subject_data:
        subject_data[subject] = []

    if avg is not None:
        subject_data[subject].append(avg)

# Calculate subject averages
subject_averages = {}

for subject, averages in subject_data.items():
    if averages:
        subject_averages[subject] = sum(averages) / len(averages)
    else:
        subject_averages[subject] = None

# Identify failing students
failing_students = [
    student for student in student_averages
    if student["average"] is not None and student["average"] < 50
]

# Print report
print("=" * 60)
print("STUDENT PERFORMANCE REPORT")
print("=" * 60)

print("\nINDIVIDUAL STUDENT AVERAGES")
print("-" * 60)

for student in student_averages:
    avg = (
        f"{student['average']:.2f}"
        if student["average"] is not None
        else "No scores available"
    )

    print(
        f"{student['name']:<10} "
        f"Subject: {student['subject']:<8} "
        f"Average: {avg}"
    )

print("\nHIGHEST SCORING STUDENT")
print("-" * 60)

if highest_student:
    print(
        f"{highest_student['name']} "
        f"({highest_student['average']:.2f})"
    )
else:
    print("No valid scores available.")

print("\nLOWEST SCORING STUDENT")
print("-" * 60)

if lowest_student:
    print(
        f"{lowest_student['name']} "
        f"({lowest_student['average']:.2f})"
    )
else:
    print("No valid scores available.")

print("\nSUBJECT AVERAGES")
print("-" * 60)

for subject, avg in subject_averages.items():
    if avg is not None:
        print(f"{subject:<10}: {avg:.2f}")
    else:
        print(f"{subject:<10}: No scores available")

print("\nFAILING STUDENTS (Average < 50)")
print("-" * 60)

if failing_students:
    for student in failing_students:
        print(
            f"{student['name']} "
            f"({student['subject']}) - "
            f"{student['average']:.2f}"
        )
else:
    print("No failing students.")

print("\n" + "=" * 60)
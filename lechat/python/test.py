# Student Score Analysis Script

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
    {"name": "Judy", "subject": "Maths", "scores": []},
]


def calculate_average(scores):
    """Calculate the average of a list of scores. Handle empty lists."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def analyze_students(students):
    """Analyze student data and return a report."""
    # Calculate average for each student
    for student in students:
        student["average"] = calculate_average(student["scores"])

    # Find highest and lowest scoring students
    valid_students = [s for s in students if s["scores"]]
    if not valid_students:
        highest = lowest = None
    else:
        highest = max(valid_students, key=lambda s: s["average"])
        lowest = min(valid_students, key=lambda s: s["average"])

    # Group by subject and calculate average per subject
    subject_data = {}
    for student in students:
        subject = student["subject"]
        if subject not in subject_data:
            subject_data[subject] = {"total": 0, "count": 0, "students": []}
        if student["scores"]:
            subject_data[subject]["total"] += student["average"]
            subject_data[subject]["count"] += 1
            subject_data[subject]["students"].append(student["name"])

    subject_averages = {
        subject: data["total"] / data["count"] if data["count"] > 0 else 0.0
        for subject, data in subject_data.items()
    }

    # Identify failing students
    failing_students = [s for s in students if s["average"] < 50]

    return {
        "students": students,
        "highest": highest,
        "lowest": lowest,
        "subject_averages": subject_averages,
        "failing_students": failing_students,
    }


def print_report(report):
    """Print a formatted report to the terminal."""
    print("=" * 50)
    print("STUDENT SCORE REPORT")
    print("=" * 50)

    # Individual student averages
    print("\n--- Individual Student Averages ---")
    for student in report["students"]:
        avg = student["average"]
        scores_str = ", ".join(map(str, student["scores"])) if student["scores"] else "No scores"
        print(f"{student['name']}: {avg:.2f} (Scores: {scores_str})")

    # Highest and lowest
    print("\n--- Highest and Lowest Scoring Students ---")
    if report["highest"]:
        print(f"Highest: {report['highest']['name']} ({report['highest']['average']:.2f})")
    else:
        print("Highest: N/A (No valid scores)")
    if report["lowest"]:
        print(f"Lowest: {report['lowest']['name']} ({report['lowest']['average']:.2f})")
    else:
        print("Lowest: N/A (No valid scores)")

    # Subject averages
    print("\n--- Subject Averages ---")
    for subject, avg in report["subject_averages"].items():
        print(f"{subject}: {avg:.2f}")

    # Failing students
    print("\n--- Failing Students (Average < 50) ---")
    if report["failing_students"]:
        for student in report["failing_students"]:
            print(f"{student['name']}: {student['average']:.2f}")
    else:
        print("None")

    print("=" * 50)


if __name__ == "__main__":
    report = analyze_students(students)
    print_report(report)
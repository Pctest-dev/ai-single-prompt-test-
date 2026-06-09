# Hardcoded list of students
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
    """Calculate average of a list of scores, handling empty lists."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def main():
    # Calculate average score for each student
    student_averages = []
    for student in students:
        avg = calculate_average(student["scores"])
        student_averages.append({
            "name": student["name"],
            "subject": student["subject"],
            "average": avg,
            "scores": student["scores"]
        })
    
    # Find highest and lowest scoring student overall
    # Filter out students with no scores for highest/lowest calculation
    students_with_scores = [s for s in student_averages if s["scores"]]
    
    if students_with_scores:
        highest_student = max(students_with_scores, key=lambda x: x["average"])
        lowest_student = min(students_with_scores, key=lambda x: x["average"])
    else:
        highest_student = lowest_student = None
    
    # Group students by subject and calculate average per subject
    subject_groups = {}
    for student in student_averages:
        subject = student["subject"]
        if subject not in subject_groups:
            subject_groups[subject] = []
        subject_groups[subject].append(student["average"])
    
    subject_averages = {}
    for subject, averages in subject_groups.items():
        # Only calculate subject average if there's at least one non-zero average
        valid_averages = [a for a in averages if a > 0 or (a == 0 and any(s["scores"] for s in students if s["subject"] == subject))]
        if valid_averages:
            subject_averages[subject] = sum(valid_averages) / len(valid_averages)
        else:
            subject_averages[subject] = 0.0
    
    # Identify failing students (average below 50, excluding those with no scores)
    failing_students = [s for s in student_averages if s["scores"] and s["average"] < 50]
    
    # Print formatted report
    print("=" * 60)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 60)
    
    # Student averages
    print("\n1. INDIVIDUAL STUDENT AVERAGES:")
    print("-" * 40)
    for student in student_averages:
        if student["scores"]:
            print(f"{student['name']:10} ({student['subject']:8}): {student['average']:.2f}")
        else:
            print(f"{student['name']:10} ({student['subject']:8}): No scores available")
    
    # Highest and lowest scoring students
    print("\n2. HIGHEST AND LOWEST SCORING STUDENTS OVERALL:")
    print("-" * 40)
    if highest_student:
        print(f"Highest: {highest_student['name']} ({highest_student['subject']}) - {highest_student['average']:.2f}")
        print(f"Lowest:  {lowest_student['name']} ({lowest_student['subject']}) - {lowest_student['average']:.2f}")
    else:
        print("No students with valid scores to determine highest/lowest.")
    
    # Subject averages
    print("\n3. AVERAGE SCORE PER SUBJECT:")
    print("-" * 40)
    for subject in sorted(subject_averages.keys()):
        print(f"{subject:10}: {subject_averages[subject]:.2f}")
    
    # Failing students
    print("\n4. FAILING STUDENTS (Average below 50):")
    print("-" * 40)
    if failing_students:
        for student in failing_students:
            print(f"{student['name']:10} ({student['subject']:8}): {student['average']:.2f}")
    else:
        print("No failing students found.")
    
    print("\n" + "=" * 60)
    print("END OF REPORT")
    print("=" * 60)

if __name__ == "__main__":
    main()
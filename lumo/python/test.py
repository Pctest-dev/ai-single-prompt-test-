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
    """Calculate average of a list of scores. Returns None if list is empty."""
    if not scores:
        return None
    return sum(scores) / len(scores)


def main():
    # Calculate individual student averages and store them
    student_data = []
    for student in students:
        avg_score = calculate_average(student["scores"])
        student_data.append({
            "name": student["name"],
            "subject": student["subject"],
            "scores": student["scores"],
            "average": avg_score
        })
    
    # Find highest and lowest scoring students (only those with scores)
    students_with_scores = [s for s in student_data if s["average"] is not None]
    
    if students_with_scores:
        highest_student = max(students_with_scores, key=lambda x: x["average"])
        lowest_student = min(students_with_scores, key=lambda x: x["average"])
    else:
        highest_student = None
        lowest_student = None
    
    # Group students by subject
    subjects = {}
    for student in student_data:
        subject = student["subject"]
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(student)
    
    # Calculate subject averages
    subject_averages = {}
    for subject, students_in_subject in subjects.items():
        valid_scores = [s["average"] for s in students_in_subject if s["average"] is not None]
        if valid_scores:
            subject_averages[subject] = sum(valid_scores) / len(valid_scores)
        else:
            subject_averages[subject] = None
    
    # Find failing students (average below 50)
    failing_students = [s for s in student_data if s["average"] is not None and s["average"] < 50]
    
    # Print formatted report
    print("=" * 60)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 60)
    
    # Individual Student Averages
    print("\n--- Individual Student Averages ---")
    print(f"{'Name':<15} {'Subject':<12} {'Average Score':>15}")
    print("-" * 42)
    for s in student_data:
        avg_str = f"{s['average']:.2f}" if s["average"] is not None else "No scores"
        print(f"{s['name']:<15} {s['subject']:<12} {avg_str:>15}")
    
    # Highest and Lowest Performers
    print("\n--- Top & Bottom Performers ---")
    if highest_student:
        print(f"Highest Scoring: {highest_student['name']} ({highest_student['subject']}) - {highest_student['average']:.2f}")
    else:
        print("Highest Scoring: No valid scores found")
    
    if lowest_student:
        print(f"Lowest Scoring:  {lowest_student['name']} ({lowest_student['subject']}) - {lowest_student['average']:.2f}")
    else:
        print("Lowest Scoring:  No valid scores found")
    
    # Subject-wise Summary
    print("\n--- Subject-wise Averages ---")
    print(f"{'Subject':<15} {'Students':>10} {'Subject Average':>18}")
    print("-" * 43)
    for subject in sorted(subject_averages.keys()):
        count = len(subjects[subject])
        avg = subject_averages[subject]
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"{subject:<15} {count:>10} {avg_str:>18}")
    
    # Failing Students
    print("\n--- Students Needing Attention (Below 50) ---")
    if failing_students:
        print(f"{'Name':<15} {'Subject':<12} {'Average':>15}")
        print("-" * 42)
        for s in failing_students:
            print(f"{s['name']:<15} {s['subject']:<12} {s['average']:.2f}")
    else:
        print("No students are currently failing.")
    
    # Edge Case Note
    students_without_scores = [s for s in student_data if s["average"] is None]
    if students_without_scores:
        print("\n--- Students Without Scores ---")
        for s in students_without_scores:
            print(f"- {s['name']} ({s['subject']}): No exam scores recorded")
    
    print("\n" + "=" * 60)
    print("End of Report")
    print("=" * 60)


if __name__ == "__main__":
    main()
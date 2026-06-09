def calculate_average(scores):
    """Calculate average of a list of scores, handling empty lists."""
    if not scores:
        return None
    return sum(scores) / len(scores)

def main():
    # Hardcoded student data
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
    
    # Calculate averages for each student and store in a new structure
    students_with_averages = []
    for student in students:
        avg_score = calculate_average(student["scores"])
        students_with_averages.append({
            **student,
            "average": avg_score,
            "has_scores": len(student["scores"]) > 0
        })
    
    # Find highest and lowest scoring students (excluding those with no scores)
    valid_students = [s for s in students_with_averages if s["has_scores"]]
    
    if not valid_students:
        print("No students have valid scores to determine highest/lowest.")
        highest_student = None
        lowest_student = None
    else:
        highest_student = max(valid_students, key=lambda x: x["average"])
        lowest_student = min(valid_students, key=lambda x: x["average"])
    
    # Group students by subject and calculate average per subject
    subjects = {}
    for student in valid_students:
        subject = student["subject"]
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(student)
    
    subject_averages = {}
    for subject, subject_students in subjects.items():
        total_avg = sum(s["average"] for s in subject_students) / len(subject_students)
        subject_averages[subject] = round(total_avg, 2)
    
    # Identify failing students (average below 50)
    failing_students = [s for s in valid_students if s["average"] < 50]
    
    # Print formatted report
    print("=" * 60)
    print("STUDENT PERFORMANCE REPORT")
    print("=" * 60)
    
    # Individual student details
    print("\n--- STUDENT DETAILS ---")
    print(f"{'Name':<12} {'Subject':<10} {'Scores':<25} {'Average':>8}")
    print("-" * 60)
    
    for student in students_with_averages:
        scores_str = str(student["scores"]) if student["has_scores"] else "N/A"
        avg_str = f"{student['average']:.2f}" if student["has_scores"] else "N/A"
        print(f"{student['name']:<12} {student['subject']:<10} {scores_str:<25} {avg_str:>8}")
    
    # Overall highest/lowest
    print("\n--- OVERALL EXTREMES ---")
    if highest_student:
        print(f"Highest scoring student: {highest_student['name']} ({highest_student['average']:.2f})")
    else:
        print("No valid data for highest scoring student.")
    
    if lowest_student:
        print(f"Lowest scoring student:  {lowest_student['name']} ({lowest_student['average']:.2f})")
    else:
        print("No valid data for lowest scoring student.")
    
    # Subject averages
    print("\n--- SUBJECT AVERAGES ---")
    for subject in sorted(subject_averages.keys()):
        avg = subject_averages[subject]
        count = len(subjects[subject])
        print(f"{subject:<12}: {avg:.2f} (based on {count} student(s))")
    
    # Failing students
    print("\n--- FAILING STUDENTS (Average < 50) ---")
    if failing_students:
        for student in failing_students:
            print(f"- {student['name']}: {student['average']:.2f}")
    else:
        print("No failing students found.")
    
    # Summary
    print("\n--- SUMMARY ---")
    print(f"Total students: {len(students)}")
    print(f"Students with scores: {len(valid_students)}")
    print(f"Subjects covered: {', '.join(sorted(subjects.keys()))}")
    
    if highest_student and lowest_student:
        diff = highest_student["average"] - lowest_student["average"]
        print(f"Difference between highest and lowest averages: {diff:.2f}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()

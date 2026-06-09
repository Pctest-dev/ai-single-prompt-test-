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


def average(scores):
    return sum(scores) / len(scores) if scores else None


def build_student_averages(students):
    return [
        {**s, "average": average(s["scores"])}
        for s in students
    ]


def find_highest_lowest(students_with_avg):
    scored = [s for s in students_with_avg if s["average"] is not None]
    if not scored:
        return None, None
    highest = max(scored, key=lambda s: s["average"])
    lowest = min(scored, key=lambda s: s["average"])
    return highest, lowest


def group_by_subject(students_with_avg):
    groups = {}
    for s in students_with_avg:
        groups.setdefault(s["subject"], []).append(s)
    subject_averages = {}
    for subject, members in groups.items():
        scored = [s["average"] for s in members if s["average"] is not None]
        subject_averages[subject] = sum(scored) / len(scored) if scored else None
    return groups, subject_averages


def find_failing(students_with_avg, threshold=50):
    return [s for s in students_with_avg if s["average"] is not None and s["average"] < threshold]


def print_report(students_with_avg):
    width = 60
    sep = "=" * width
    thin = "-" * width

    print(sep)
    print("STUDENT PERFORMANCE REPORT".center(width))
    print(sep)

    # Per-student averages
    print("\nINDIVIDUAL RESULTS")
    print(thin)
    print(f"{'Name':<10} {'Subject':<10} {'Scores':<25} {'Average':>7}")
    print(thin)
    for s in students_with_avg:
        scores_str = str(s["scores"]) if s["scores"] else "No scores"
        avg_str = f"{s['average']:.2f}" if s["average"] is not None else "N/A"
        print(f"{s['name']:<10} {s['subject']:<10} {scores_str:<25} {avg_str:>7}")

    # Highest and lowest
    highest, lowest = find_highest_lowest(students_with_avg)
    print(f"\n{'OVERALL STANDINGS'}")
    print(thin)
    if highest:
        print(f"  Highest scorer : {highest['name']} ({highest['average']:.2f})")
    if lowest:
        print(f"  Lowest scorer  : {lowest['name']} ({lowest['average']:.2f})")

    # Subject averages
    groups, subject_averages = group_by_subject(students_with_avg)
    print(f"\nSUBJECT AVERAGES")
    print(thin)
    for subject in sorted(subject_averages):
        avg = subject_averages[subject]
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        members = ", ".join(s["name"] for s in groups[subject])
        print(f"  {subject:<10} {avg_str:>6}  ({members})")

    # Failing students
    failing = find_failing(students_with_avg)
    print(f"\nFAILING STUDENTS (average < 50)")
    print(thin)
    if failing:
        for s in failing:
            print(f"  {s['name']:<10} {s['subject']:<10} avg: {s['average']:.2f}")
    else:
        print("  None")

    # Students with no scores
    no_scores = [s for s in students_with_avg if s["average"] is None]
    if no_scores:
        print(f"\nSTUDENTS WITH NO SCORES")
        print(thin)
        for s in no_scores:
            print(f"  {s['name']} ({s['subject']}) — no scores recorded")

    print(f"\n{sep}\n")


def main():
    students_with_avg = build_student_averages(students)
    print_report(students_with_avg)


if __name__ == "__main__":
    main()

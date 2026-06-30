def calculate_average(scores):
    """Calculate the average of a list of scores. Returns 0 for an empty list."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def build_student_averages(students):
    """Return a list of (name, subject, average) tuples."""
    result = []
    for student in students:
        avg = calculate_average(student["scores"])
        result.append((student["name"], student["subject"], avg))
    return result


def find_extreme_students(averages):
    """Find highest and lowest scoring students. Returns (highest, lowest).

    Students with an empty score list (average 0.0) are treated as not having
    a valid average and are excluded from the extreme calculation.
    """
    valid = [(n, s, a) for (n, s, a) in averages if a > 0]
    if not valid:
        return None, None
    highest = max(valid, key=lambda x: x[2])
    lowest = min(valid, key=lambda x: x[2])
    return highest, lowest


def group_by_subject(averages):
    """Group students by subject and return per-subject average.

    Returns a dict: subject -> (average, list of (name, average)).
    """
    groups = {}
    for name, subject, avg in averages:
        groups.setdefault(subject, []).append((name, avg))

    subject_summary = {}
    for subject, members in groups.items():
        valid_avgs = [a for (_, a) in members if a > 0]
        if valid_avgs:
            subj_avg = sum(valid_avgs) / len(valid_avgs)
        else:
            subj_avg = 0.0
        subject_summary[subject] = (subj_avg, members)
    return subject_summary


def find_failing_students(averages, threshold=50.0):
    """Return list of (name, subject, average) for students failing.

    A student with no scores (empty list) is not counted as failing since
    there is no data to evaluate; only students whose average is below the
    threshold (and who have scores) are flagged.
    """
    failing = []
    for name, subject, avg in averages:
        if avg > 0 and avg < threshold:
            failing.append((name, subject, avg))
    return failing


def print_report(students):
    """Print the full formatted report to the terminal."""
    line = "=" * 60

    averages = build_student_averages(students)
    highest, lowest = find_extreme_students(averages)
    subject_summary = group_by_subject(averages)
    failing = find_failing_students(averages)

    print(line)
    print("STUDENT PERFORMANCE REPORT".center(60))
    print(line)

    # Per-student averages
    print("\nPer-Student Averages")
    print("-" * 60)
    print(f"{'Name':<12}{'Subject':<12}{'Average':>10}  {'Status':<14}")
    print("-" * 60)
    for name, subject, avg in averages:
        if avg == 0:
            status = "NO SCORES"
        elif avg < 50:
            status = "FAILING"
        else:
            status = "PASSING"
        print(f"{name:<12}{subject:<12}{avg:>10.2f}  {status:<14}")

    # Highest / lowest
    print("\n" + line)
    print("Overall Standouts")
    print("-" * 60)
    if highest:
        print(f"Highest scorer : {highest[0]} ({highest[1]}) - {highest[2]:.2f}")
    else:
        print("Highest scorer : N/A (no valid scores)")
    if lowest:
        print(f"Lowest scorer  : {lowest[0]} ({lowest[1]}) - {lowest[2]:.2f}")
    else:
        print("Lowest scorer  : N/A (no valid scores)")

    # Subject groupings
    print("\n" + line)
    print("Subject Group Averages")
    print("-" * 60)
    print(f"{'Subject':<12}{'Average':>10}  {'Students':<30}")
    print("-" * 60)
    for subject in sorted(subject_summary):
        subj_avg, members = subject_summary[subject]
        member_names = ", ".join(m[0] for m in members)
        print(f"{subject:<12}{subj_avg:>10.2f}  {member_names:<30}")

    # Failing students
    print("\n" + line)
    print("Failing Students (average below 50)")
    print("-" * 60)
    if failing:
        for name, subject, avg in failing:
            print(f"  {name:<12}({subject}) - {avg:.2f}")
    else:
        print("  None")

    # Edge case note for empty score lists
    empty = [(n, s) for (n, s, a) in averages if a == 0]
    if empty:
        print("\n" + line)
        print("Students With No Score Data (excluded from rankings)")
        print("-" * 60)
        for name, subject in empty:
            print(f"  {name:<12}({subject})")

    print("\n" + line)
    print("End of Report".center(60))
    print(line)


if __name__ == "__main__":
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

    print_report(students)

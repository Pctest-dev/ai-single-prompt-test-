#!/usr/bin/env python3
"""
Student performance report

This script analyses a hard‑coded list of students.
For each student it calculates the average score, determines the overall best and worst
students, groups students by subject to compute subject averages,
and flags any failing students (average < 50).

No external libraries are used – only the Python standard library.
"""

# --------------------------- data ------------------------------------
students = [
    {"name": "Alice",   "subject": "Maths",   "scores": [85, 92, 78, 90]},
    {"name": "Bob",     "subject": "Science", "scores": [45, 52, 38, 41]},
    {"name": "Carol",   "subject": "Maths",   "scores": [72, 68, 75, 80]},
    {"name": "David",   "subject": "English", "scores": [55, 60, 58, 62]},
    {"name": "Eve",     "subject": "Science", "scores": [90, 95, 88, 92]},
    {"name": "Frank",   "subject": "English", "scores": [30, 25, 40, 35]},
    {"name": "Grace",   "subject": "Maths",   "scores": [65, 70, 68, 72]},
    {"name": "Heidi",   "subject": "Science", "scores": [48, 45, 50, 47]},
    {"name": "Ivan",    "subject": "English", "scores": [88, 92, 85, 90]},
    {"name": "Judy",    "subject": "Maths",   "scores": []}
]

# --------------------------- helper functions -----------------------
def calc_average(scores):
    """Return average of a list of numbers.
       If the list is empty return None."""
    if not scores:
        return None
    return sum(scores) / len(scores)

def format_avg(avg):
    """Return formatted average or 'N/A'."""
    return f"{avg:.2f}" if avg is not None else "N/A"

# --------------------------- main analysis -------------------------
def analyze(students):
    # 1. Compute per‑student averages
    for student in students:
        student['average'] = calc_average(student['scores'])

    # 2. Find highest & lowest scoring students (ignore those with no scores)
    best_student = None
    worst_student = None
    best_avg = -1e9
    worst_avg = 1e9

    for student in students:
        avg = student.get('average')
        if avg is None:   # skip students without any scores
            continue
        if avg > best_avg:
            best_avg = avg
            best_student = student
        if avg < worst_avg:
            worst_avg = avg
            worst_student = student

    # 3. Group by subject and compute subject averages
    subject_stats = {}   # subject -> {'total': x, 'count': y}
    for student in students:
        subj = student['subject']
        scores = student['scores']
        if subj not in subject_stats:
            subject_stats[subj] = {'total': 0, 'count': 0}
        subject_stats[subj]['total'] += sum(scores)
        subject_stats[subj]['count'] += len(scores)

    subject_averages = {}
    for subj, stats in subject_stats.items():
        count = stats['count']
        avg = (stats['total'] / count) if count > 0 else None
        subject_averages[subj] = avg

    # 4. Identify failing students
    failing_students = [
        s for s in students
        if s.get('average') is not None and s['average'] < 50
    ]

    return {
        'students': students,
        'best_student': best_student,
        'worst_student': worst_student,
        'subject_averages': subject_averages,
        'failing_students': failing_students
    }

# --------------------------- reporting --------------------------------
def print_report(results):
    print("\n=== Student Averages ===")
    header = f"{'Name':<10} {'Subject':<8} {'Average':>7}"
    print(header)
    print("-" * len(header))
    for s in results['students']:
        name = s['name']
        subj = s['subject']
        avg_str = format_avg(s.get('average'))
        print(f"{name:<10} {subj:<8} {avg_str:>7}")

    # Highest & lowest
    best = results['best_student']
    worst = results['worst_student']

    if best:
        print("\nHighest scoring student:")
        print(f"  {best['name']} ({format_avg(best['average'])})")
    else:
        print("\nNo data to determine highest scorer.")

    if worst:
        print("Lowest  scoring student:")
        print(f"  {worst['name']} ({format_avg(worst['average'])})")
    else:
        print("No data to determine lowest scorer.")

    # Subject averages
    print("\n=== Average Score per Subject ===")
    for subj, avg in results['subject_averages'].items():
        print(f"  {subj:<8} : {format_avg(avg)}")

    # Failing students
    failing = results['failing_students']
    if failing:
        print("\n=== Students Failing (Average < 50) ===")
        for s in failing:
            print(f"  {s['name']} ({format_avg(s['average'])})")
    else:
        print("\nNo students are failing.")

# --------------------------- entry point --------------------------------
if __name__ == "__main__":
    analysis_results = analyze(students)
    print_report(analysis_results)

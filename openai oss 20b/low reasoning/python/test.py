#!/usr/bin/env python3
"""
Student performance report

This script:
1. Calculates each student's average exam score.
2. Finds the highest and lowest scoring students overall.
3. Groups students by subject and calculates the average score per subject.
4. Flags any student whose average is below 50 as failing.
5. Prints a nicely formatted report.

No external libraries are used – only the Python standard library.
"""

# ----------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------
students = [
    {"name": "Alice",   "subject": "Maths",    "scores": [85, 92, 78, 90]},
    {"name": "Bob",     "subject": "Science",  "scores": [45, 52, 38, 41]},
    {"name": "Carol",   "subject": "Maths",    "scores": [72, 68, 75, 80]},
    {"name": "David",   "subject": "English",  "scores": [55, 60, 58, 62]},
    {"name": "Eve",     "subject": "Science",  "scores": [90, 95, 88, 92]},
    {"name": "Frank",   "subject": "English",  "scores": [30, 25, 40, 35]},
    {"name": "Grace",   "subject": "Maths",    "scores": [65, 70, 68, 72]},
    {"name": "Heidi",   "subject": "Science",  "scores": [48, 45, 50, 47]},
    {"name": "Ivan",    "subject": "English",  "scores": [88, 92, 85, 90]},
    {"name": "Judy",    "subject": "Maths",    "scores": []},
]

# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------
def average(scores):
    """Return the arithmetic mean of a list of numbers.
    If the list is empty, return None."""
    if not scores:
        return None
    return sum(scores) / len(scores)

def format_avg(avg):
    """Format an average for printing – 2 decimals or 'N/A'."""
    return f"{avg:.2f}" if avg is not None else "N/A"

# ----------------------------------------------------------------------
# Main analysis
# ----------------------------------------------------------------------
# 1. Compute each student's average and store it in a new key.
for student in students:
    student["average"] = average(student["scores"])

# 2. Find highest/lowest scoring students (based on the computed averages).
valid_students = [s for s in students if s["average"] is not None]
if valid_students:
    highest_student = max(valid_students, key=lambda s: s["average"])
    lowest_student  = min(valid_students, key=lambda s: s["average"])
else:
    highest_student = lowest_student = None

# 3. Group by subject and compute subject averages.
subject_totals = {}
subject_counts = {}

for student in students:
    subj = student["subject"]
    avg = student["average"]
    if avg is not None:
        subject_totals.setdefault(subj, 0.0)
        subject_counts.setdefault(subj, 0)
        subject_totals[subj] += avg
        subject_counts[subj] += 1

subject_averages = {}
for subj in subject_totals:
    subject_averages[subj] = subject_totals[subj] / subject_counts[subj]

# 4. Identify failing students (average < 50).
failing_students = [s for s in students if s["average"] is not None and s["average"] < 50]

# ----------------------------------------------------------------------
# Report printing
# ----------------------------------------------------------------------
print("\n===== Student Performance Report =====\n")

print("1. Individual Averages")
print("-----------------------")
for student in students:
    name = student["name"]
    subj = student["subject"]
    avg_str = format_avg(student["average"])
    print(f"  {name:<6} ({subj:7}) : {avg_str}")

print("\n2. Highest & Lowest Scorers")
print("---------------------------")
if highest_student:
    print(f"  Highest: {highest_student['name']} ({format_avg(highest_student['average'])})")
else:
    print("  No valid scores to determine highest scorer.")

if lowest_student:
    print(f"  Lowest : {lowest_student['name']} ({format_avg(lowest_student['average'])})")
else:
    print("  No valid scores to determine lowest scorer.")

print("\n3. Subject Averages")
print("--------------------")
for subj, avg in subject_averages.items():
    print(f"  {subj:<7} : {avg:.2f}")

print("\n4. Failing Students (average < 50)")
print("---------------------------------")
if failing_students:
    for s in failing_students:
        print(f"  {s['name']} ({format_avg(s['average'])})")
else:
    print("  None – all students passed.")

print("\n===== End of Report =====\n")

#!/usr/bin/env python3
"""
Student score analysis script.

Given a hard‑coded list of students (each with a name, subject and exam scores),
this script:
  • Calculates the average score for each student.
  • Finds the highest‑ and lowest‑scoring student overall.
  • Groups students by subject and calculates the average score per subject.
  • Identifies any failing students (average < 50).
  • Prints a formatted report to the terminal.

Edge cases such as empty score lists are handled gracefully – averages are
reported as “N/A” where appropriate. No external libraries are required; only
Python's standard library is used.
"""

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
    {"name": "Judy",    "subject": "Maths",    "scores": []}
]

def calculate_average(scores):
    """Return the average of a list of numbers.
    Return None if the list is empty."""
    return sum(scores) / len(scores) if scores else None

def format_avg(avg):
    """Format an average for printing: two decimal places or 'N/A'."""
    return f"{avg:.2f}" if avg is not None else "N/A"

def main():
    # 1. Calculate the average score for each student
    student_averages = []
    for s in students:
        avg = calculate_average(s.get("scores", []))
        student_averages.append({
            "name":     s["name"],
            "subject":  s["subject"],
            "average":  avg
        })

    # 2. Find the highest‑ and lowest‑scoring students (by average)
    valid_students = [s for s in student_averages if s["average"] is not None]
    highest_student = max(valid_students, key=lambda x: x["average"]) if valid_students else None
    lowest_student  = min(valid_students, key=lambda x: x["average"]) if valid_students else None

    # 3. Group students by subject and calculate the average score per subject
    subject_scores = {}
    for s in students:
        subj = s["subject"]
        subject_scores.setdefault(subj, []).extend(s.get("scores", []))
    subject_averages = {subj: calculate_average(scores) for subj, scores in subject_scores.items()}

    # 4. Identify any failing students (average < 50)
    failing_students = [
        s for s in student_averages
        if s["average"] is not None and s["average"] < 50
    ]

    # 5. Print a formatted report to the terminal
    print("\nStudent Averages:")
    for s in sorted(student_averages, key=lambda x: x["name"]):
        print(f"  {s['name']} ({s['subject']}) - Average: {format_avg(s['average'])}")

    if highest_student:
        print("\nHighest Scoring Student:")
        print(f"  {highest_student['name']} ({highest_student['subject']}) "
              f"- Average: {format_avg(highest_student['average'])}")
    else:
        print("\nNo valid student averages to determine the highest scorer.")

    if lowest_student:
        print("\nLowest Scoring Student:")
        print(f"  {lowest_student['name']} ({lowest_student['subject']}) "
              f"- Average: {format_avg(lowest_student['average'])}")
    else:
        print("\nNo valid student averages to determine the lowest scorer.")

    print("\nAverage Score per Subject:")
    for subj in sorted(subject_averages):
        print(f"  {subj}: {format_avg(subject_averages[subj])}")

    print("\nFailing Students (average below 50):")
    if failing_students:
        for s in sorted(failing_students, key=lambda x: x["name"]):
            print(f"  {s['name']} ({s['subject']}) - Average: {format_avg(s['average'])}")
    else:
        print("  None")

if __name__ == "__main__":
    main()

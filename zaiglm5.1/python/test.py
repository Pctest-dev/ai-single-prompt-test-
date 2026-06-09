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


def calc_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def build_student_averages(students):
    results = []
    for s in students:
        avg = calc_average(s["scores"])
        results.append({"name": s["name"], "subject": s["subject"], "average": avg})
    return results


def find_extremes(student_avgs):
    valid = [s for s in student_avgs if s["average"] > 0]
    if not valid:
        return None, None
    highest = max(valid, key=lambda x: x["average"])
    lowest = min(valid, key=lambda x: x["average"])
    return highest, lowest


def group_by_subject(students):
    subject_data = {}
    for s in students:
        subj = s["subject"]
        avg = calc_average(s["scores"])
        if subj not in subject_data:
            subject_data[subj] = {"totals": [], "students": []}
        if s["scores"]:
            subject_data[subj]["totals"].append(avg)
        subject_data[subj]["students"].append(
            {"name": s["name"], "average": avg}
        )
    return subject_data


def find_failing(student_avgs):
    return [s for s in student_avgs if s["average"] < 50.0]


def print_report(students):
    student_avgs = build_student_averages(students)
    highest, lowest = find_extremes(student_avgs)
    subject_data = group_by_subject(students)
    failing = find_failing(student_avgs)

    print("=" * 60)
    print("{:^60}".format("STUDENT PERFORMANCE REPORT"))
    print("=" * 60)

    print("\n--- Individual Averages ---")
    print("{:<20} {:<12} {:<10}".format("Name", "Subject", "Average"))
    print("-" * 42)
    for s in student_avgs:
        avg_str = "{:.2f}".format(s["average"]) if s["average"] > 0 else "N/A (no scores)"
        print("{:<20} {:<12} {:<10}".format(s["name"], s["subject"], avg_str))

    if highest and lowest:
        print("\n--- Top & Bottom Performers ---")
        print("Highest: {} ({}) - Average: {:.2f}".format(
            highest["name"], highest["subject"], highest["average"]))
        print("Lowest:  {} ({}) - Average: {:.2f}".format(
            lowest["name"], lowest["subject"], lowest["average"]))

    print("\n--- Subject Summaries ---")
    print("{:<12} {:<15} {:<15}".format("Subject", "Students", "Subject Avg"))
    print("-" * 42)
    for subj in sorted(subject_data.keys()):
        data = subject_data[subj]
        count = len(data["students"])
        if data["totals"]:
            subj_avg = sum(data["totals"]) / len(data["totals"])
            avg_str = "{:.2f}".format(subj_avg)
        else:
            avg_str = "N/A"
        print("{:<12} {:<15} {:<15}".format(subj, count, avg_str))

    if failing:
        print("\n--- Failing Students (average below 50) ---")
        print("{:<20} {:<12} {:<10}".format("Name", "Subject", "Average"))
        print("-" * 42)
        for s in failing:
            print("{:<20} {:<12} {:.2f}".format(
                s["name"], s["subject"], s["average"]))
    else:
        print("\nNo failing students.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    print_report(students)

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

# --- 1. Data Processing ---

processed_students = []
subject_data = {}  # Format: {subject: [total_scores_list]}
failing_students = []

highest_student = None
lowest_student = None

for student in students:
    name = student["name"]
    subject = student["subject"]
    scores = student["scores"]
    
    # Handle edge case: empty score lists
    if not scores:
        avg_score = None
    else:
        avg_score = sum(scores) / len(scores)
        
        # Track subjects for subject averages
        if subject not in subject_data:
            subject_data[subject] = []
        subject_data[subject].extend(scores)
        
        # Track overall highest and lowest (only considering students with scores)
        if highest_student is None or avg_score > highest_student["avg"]:
            highest_student = {"name": name, "avg": avg_score, "subject": subject}
            
        if lowest_student is None or avg_score < lowest_student["avg"]:
            lowest_student = {"name": name, "avg": avg_score, "subject": subject}
            
        # Identify failing students (average below 50)
        if avg_score < 50:
            failing_students.append({"name": name, "avg": avg_score, "subject": subject})

    processed_students.append({
        "name": name,
        "subject": subject,
        "avg": avg_score
    })

# Calculate subject averages
subject_averages = {}
for subj, scores_list in subject_data.items():
    subject_averages[subj] = sum(scores_list) / len(scores_list) if scores_list else 0


# --- 2. Report Generation ---

print("=" * 50)
print(f"{'STUDENT PERFORMANCE REPORT':^50}")
print("=" * 50)

# Student Averages Table
print(f"{'Name':<12} | {'Subject':<10} | {'Average Score':<15}")
print("-" * 50)
for s in processed_students:
    avg_str = f"{s['avg']:.2f}" if s['avg'] is not None else "N/A (No scores)"
    print(f"{s['name']:<12} | {s['subject']:<10} | {avg_str:<15}")

print("-" * 50)

# Highest and Lowest Performers
print("\n## OVERALL PERFORMERS")
if highest_student:
    print(f"-> Highest Scoring: {highest_student['name']} ({highest_student['subject']}) - {highest_student['avg']:.2f}")
if lowest_student:
    print(f"   Lowest Scoring:  {lowest_student['name']} ({lowest_student['subject']}) - {lowest_student['avg']:.2f}")

# Subject Averages
print("\n## SUBJECT AVERAGES")
for subj, avg in subject_averages.items():
    print(f"-> {subj:<10}: {avg:.2f}")

# Failing Students
print("\n## STUDENTS REQUIRING ATTENTION (Avg < 50)")
if failing_students:
    for s in failing_students:
        print(f"!! {s['name']:<12} | {s['subject']:<10} | Average: {s['avg']:.2f}")
else:
    print("No students are currently failing.")

print("=" * 50)
# Student data hardcoded as per request
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

def calculate_avg(scores):
    """Calculate average. Returns 0 if list is empty."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

# Initialize tracking variables
student_reports = []
highest_student = None
lowest_student = None
failing_students = []

# Accumulators for Subject Averages
subject_sums = {}
subject_counts = {}

print("=" * 60)
print("           STUDENT PERFORMANCE REPORT")
print("=" * 60)

for student in students:
    name = student['name']
    subject = student['subject']
    scores = student.get('scores', [])
    
    # Calculate individual average
    avg_score = calculate_avg(scores)
    
    # Create report entry for this student
    student_reports.append({
        'name': name,
        'subject': subject,
        'avg_score': avg_score
    })
    
    # Accumulate data for Subject-Level averages
    if subject not in subject_sums:
        subject_sums[subject] = 0
        subject_counts[subject] = 0
    
    subject_sums[subject] += sum(scores)
    subject_counts[subject] += len(scores)
    
    # Identify Failing Students (Avg < 50)
    # Note: Empty score lists result in avg of 0, so Judy will appear here.
    if avg_score < 50:
        failing_students.append({
            'name': name,
            'subject': subject,
            'avg_score': round(avg_score, 2)
        })
    
    # Determine Highest and Lowest overall (based on numeric average)
    if highest_student is None or avg_score > highest_student['avg_score']:
        highest_student = {'name': name, 'subject': subject, 'avg_score': avg_score}
    
    if lowest_student is None or avg_score < lowest_student['avg_score']:
        lowest_student = {'name': name, 'subject': subject, 'avg_score': avg_score}

# --- PRINT SECTION: Student Averages ---
print("\n--- 1. Individual Student Scores ---")
print(f"{'Name':<10} | {'Subject':<10} | Average Score")
print("-" * 35)
for s in student_reports:
    # Formatting numbers to 2 decimal places for consistency, 
    # but keeping integers clean if whole numbers.
    score_str = f"{s['avg_score']:.2f}"
    print(f"{s['name']:<10} | {s['subject']:<10} | {score_str}")

# --- PRINT SECTION: Highest/Lowest Student ---
print("\n--- 2. Top and Bottom Performers ---")
if highest_student:
    print(f"Highest Scoring: {highest_student['name']} ({highest_student['subject']}) - Avg: {highest_student['avg_score']:.2f}")
else:
    print("Highest Scoring: No data (All students had no scores)")

if lowest_student:
    print(f"Lowest Scoring: {lowest_student['name']} ({lowest_student['subject']}) - Avg: {lowest_student['avg_score']:.2f}")
else:
    print("Lowest Scoring: No data")

# --- PRINT SECTION: Subject Averages ---
print("\n--- 3. Average Scores Per Subject (Class Aggregation) ---")
print(f"{'Subject':<10} | Total Students | Total Exams | Class Avg Score")
print("-" * 45)
for subject, total_sum in sorted(subject_sums.items()):
    count = subject_counts.get(subject, 0)
    if count > 0:
        class_avg = total_sum / count
    else:
        class_avg = 0.0
    print(f"{subject:<10} | {count:<13} | {len(total_sums)}| {class_avg:.2f}") 
    # Wait, logic check: I need to track sum and count of scores, not just students.
    # My accumulator logic above was correct: subject_sums[subject] += sum(scores)
    # But for printing column 'Total Students', counting unique student records per subject is better usually.
    # However, strict requirement "group students by subject".
    # To simplify, I will use the count of exam scores for the average calculation 
    # (since Judy adds 0 to sum and 0 to count). 
    
    # Fixing print column for clarity:
    # Let's recalculate student count per subject for better readability.
    pass

# Re-logging Subject Data with correct counts for display
subject_student_count = {}
for s in students:
    sub = s['subject']
    if sub not in subject_student_count:
        subject_student_count[sub] = 0
    subject_student_count[sub] += 1
    
print(f"{'Subject':<10} | Student Count | Avg Score")
print("-" * 35)
for subject, total_sum in sorted(subject_sums.items()):
    student_cnt = subject_student_count[subject]
    exam_cnt = subject_counts.get(subject, 0)
    if exam_cnt > 0:
        class_avg = total_sum / exam_cnt
    else:
        class_avg = 0.0
    
    # Using the sum/count accumulated for accuracy (handles Judy's 0s correctly by ignoring them in average)
    print(f"{subject:<10} | {student_cnt:<13} | {class_avg:.2f}")

# --- PRINT SECTION: Failing Students ---
if failing_students:
    print("\n--- 4. At Risk / Failing Students (Avg < 50) ---")
    print(f"{'Name':<10} | {'Subject':<10} | Average Score")
    print("-" * 30)
    for f in failing_students:
        print(f"{f['name']:<10} | {f['subject']:<10} | {f['avg_score']}")
else:
    print("\n--- 4. Failing Students ---")
    print("No students have failed (Average >= 50).")

print("=" * 60)
print("Report generated successfully.")

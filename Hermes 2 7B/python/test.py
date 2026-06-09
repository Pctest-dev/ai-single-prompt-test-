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

from operator import itemgetter
from collections import defaultdict

def average_scores(student_list):
    for student in student_list:
        name = student['name']
        subject = student['subject']
        scores = student['scores']
        
        if not scores:
            print(f"{name}: No data.")
            continue
        
        avg_score = sum(scores)/len(scores)
        print(f"{name} in {subject}: {avg_score:.2f}")
        
        if avg_score < 50:
            print(f"{name} is failing!")
    
    subjects = defaultdict(list)
    
    for student in student_list:
        name = student['name']
        subject = student['subject']
        
        if not student['scores']:
            continue
            
        subjects[subject].append(student['name'])
        subjects[subject].append(sum(student['scores'])/len(student['scores']))
    
    print("\nSubjects & Average Scores:")
    for key in subjects.keys():
        print(f"Subject: {key}")
        for i in subjects[key]:
            print(f"- {i}")
        
    # Finding highest and lowest
    sorted_list = sorted(student_list, key=itemgetter('name'))
    
    highest_scoring = sorted_list[0]['name']
    lowest_scoring = sorted_list[-1]['name']
    
    print("\nHighest scoring student is: ", highest_scoring)
    print("Lowest scoring student is: ", lowest_scoring)

average_scores(students)

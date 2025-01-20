"""
Creation of data for honors project.
Date: 17 Jan 2025
"""

import random
import pandas as pd

num_students = 100
num_universities = 10
min_preferences_per_student = 3
max_preferences_per_student = 5
min_slots_per_university = 5
max_slots_per_university = 20

# Generate student nodes
def generate_students(num_students, num_universities, min_preferences, max_preferences):
    students = []
    for student_id in range(1, num_students + 1):
        preferences = random.sample(range(1, num_universities + 1),
                                    k=random.randint(min_preferences, max_preferences))
        students.append({
            'Student_ID': student_id,
            'Preferences': preferences
        })
    return students

# Generate university nodes
def generate_universities(num_universities, num_students):
    total_slots_needed = num_students
    universities = []
    while sum(university['Slots'] for university in universities) < total_slots_needed:
        universities = []
        for university_id in range(1, num_universities + 1):
            slots = random.randint(min_slots_per_university, max_slots_per_university)
            universities.append({
                'University_ID': university_id,
                'Slots': slots
            })
    return universities

# Create the data
students = generate_students(num_students, num_universities, min_preferences_per_student, max_preferences_per_student)
universities = generate_universities(num_universities, num_students)

# Convert the data to DataFrames
students_df = pd.DataFrame(students)
students_df['Preferences'] = students_df['Preferences'].apply(lambda x: ','.join(map(str, x)))
universities_df = pd.DataFrame(universities)

students_df.to_csv('synthetic_students.csv', index=False)
universities_df.to_csv('synthetic_universities.csv', index=False)

print("Synthetic data generated and saved as CSV files:")
print("- synthetic_students.csv")
print("- synthetic_universities.csv")

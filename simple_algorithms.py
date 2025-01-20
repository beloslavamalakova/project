import os
import pandas as pd

# Load the synthetic datasets
students_df = pd.read_csv('synthetic_students.csv')
universities_df = pd.read_csv('synthetic_universities.csv')

# Convert data back to appropriate formats
students = [
    {
        'Student_ID': row['Student_ID'],
        'Preferences': list(map(int, row['Preferences'].split(',')))
    }
    for _, row in students_df.iterrows()
]

universities = [
    {
        'University_ID': row['University_ID'],
        'Slots': row['Slots']
    }
    for _, row in universities_df.iterrows()
]

# Serial Dictatorship Algorithm
def serial_dictatorship(students, universities):
    allocations = {}
    for student in students:
        for preference in student['Preferences']:
            if universities[preference - 1]['Slots'] > 0:
                allocations[student['Student_ID']] = preference
                universities[preference - 1]['Slots'] -= 1
                break
    return allocations

# Artificial Cap Deferred Acceptance Algorithm
def artificial_cap_deferred_acceptance(students, universities):
    allocations = {}
    proposals = {student['Student_ID']: [] for student in students}

    while True:
        changes = False
        for student in students:
            if student['Student_ID'] not in allocations:
                for preference in student['Preferences']:
                    if preference not in proposals[student['Student_ID']]:
                        proposals[student['Student_ID']].append(preference)
                        changes = True
                        break

        for university in universities:
            interested_students = [
                student_id for student_id, prefs in proposals.items()
                if university['University_ID'] in prefs and student_id not in allocations
            ]
            selected_students = interested_students[:university['Slots']]
            for student_id in selected_students:
                if student_id not in allocations:
                    allocations[student_id] = university['University_ID']
                    university['Slots'] -= 1

        if not changes:
            break

    return allocations

# Stable Matching Algorithm
def stable_matching(students, universities):
    free_students = {student['Student_ID'] for student in students}
    proposals = {student['Student_ID']: [] for student in students}
    allocations = {university['University_ID']: [] for university in universities}

    while free_students:
        for student_id in list(free_students):
            student = next(s for s in students if s['Student_ID'] == student_id)
            for preference in student['Preferences']:
                if preference not in proposals[student_id]:
                    proposals[student_id].append(preference)
                    allocations[preference].append(student_id)
                    if len(allocations[preference]) > universities[preference - 1]['Slots']:
                        removed_student = allocations[preference].pop(0)
                        free_students.add(removed_student)
                    free_students.discard(student_id)
                    break

    final_allocations = {}
    for university_id, student_list in allocations.items():
        for student_id in student_list:
            final_allocations[student_id] = university_id

    return final_allocations

# Run the algorithms
universities_copy_sd = [university.copy() for university in universities]
universities_copy_acda = [university.copy() for university in universities]
universities_copy_sm = [university.copy() for university in universities]

allocations_sd = serial_dictatorship(students, universities_copy_sd)
allocations_acda = artificial_cap_deferred_acceptance(students, universities_copy_acda)
allocations_sm = stable_matching(students, universities_copy_sm)

# Convert numpy integers to standard Python integers
allocations_sd = {int(k): int(v) for k, v in allocations_sd.items()}
allocations_acda = {int(k): int(v) for k, v in allocations_acda.items()}
allocations_sm = {int(k): int(v) for k, v in allocations_sm.items()}

# Save results to files
os.makedirs('matchings_results', exist_ok=True)

with open('matchings_results/serial_dictatorship.txt', 'w') as f:
    f.write(str(allocations_sd))

with open('matchings_results/acda.txt', 'w') as f:
    f.write(str(allocations_acda))

with open('matchings_results/stable_matching.txt', 'w') as f:
    f.write(str(allocations_sm))

# Display the results
print("Results saved in 'matchings_results' folder:")
print("- serial_dictatorship.txt")
print("- acda.txt")
print("- stable_matching.txt")

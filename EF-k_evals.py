"""""
EF-k Comparison Script

This script evaluates the fairness of matchings using the EF-k criterion as introduced in the paper
"Fairness and Efficiency Trade-off in Two-Sided Matching" by Cho et al. (2024).

### What is EF-k?
EF-k stands for "Envy-Free up to k Peers," which measures the maximum number of peers (students)
that any student envies in a given matching. It is a relaxed fairness criterion where:
- **EF-0**: No student envies any other student (strict fairness).
- **EF-(n-1)**: Any matching satisfies this, as each student can envy at most all other students.
- Intermediate values of k represent different levels of fairness, with smaller k indicating fairer matchings.

### What does the score mean?
- **Lower EF-k score**: Indicates a fairer matching, as fewer students are envied by others.
- **Higher EF-k score**: Suggests more justified envy, implying a less fair matching.

### Purpose
This script calculates and compares the EF-k scores for matchings produced by various algorithms
(Serial Dictatorship, ACDA, Stable Matching) using synthetic data and outputs the results.

"""""

import os
import pandas as pd


def load_matching(file_path):
    """Load a matching from a text file."""
    with open(file_path, 'r') as f:
        return eval(f.read())


def is_envy_justified(student, other_student, assigned_college, other_college, preferences, college_prefs):
    """Check if student has justified envy towards another student."""
    if not assigned_college or not other_college:
        return False

    if other_college in preferences.get(student['Student_ID'], []):
        student_rank = preferences[student['Student_ID']].index(other_college)
        assigned_rank = preferences[student['Student_ID']].index(assigned_college) if assigned_college else float('inf')

        other_student_rank = college_prefs[other_college].index(other_student['Student_ID'])
        student_rank_in_college = college_prefs[other_college].index(student['Student_ID'])

        return student_rank < assigned_rank and student_rank_in_college < other_student_rank

    return False


def calculate_ef_k(matching, students, colleges):
    """Calculate the EF-k score for a given matching."""
    # Student preferences
    preferences = {
        student['Student_ID']: student['Preferences'] for student in students
    }

    # College preferences (e.g., students in order of their IDs)
    college_prefs = {
        college['University_ID']: [student['Student_ID'] for student in students]
        for college in colleges
    }

    envy_counts = {student['Student_ID']: 0 for student in students}

    for student in students:
        student_id = student['Student_ID']
        assigned_college = matching.get(student_id)

        for other_student in students:
            if student_id == other_student['Student_ID']:
                continue

            other_college = matching.get(other_student['Student_ID'])
            if other_college and other_college in college_prefs:
                # Safely handle rank retrieval in student preferences
                assigned_rank = (
                    preferences[student_id].index(assigned_college)
                    if assigned_college in preferences[student_id]
                    else float('inf')
                )
                other_college_rank = (
                    preferences[student_id].index(other_college)
                    if other_college in preferences[student_id]
                    else float('inf')
                )

                # Safely handle rank retrieval in college preferences
                other_student_rank = (
                    college_prefs[other_college].index(other_student['Student_ID'])
                    if other_student['Student_ID'] in college_prefs[other_college]
                    else float('inf')
                )
                student_rank_in_college = (
                    college_prefs[other_college].index(student_id)
                    if student_id in college_prefs[other_college]
                    else float('inf')
                )

                # Check for justified envy
                if (
                    other_college_rank < assigned_rank and
                    student_rank_in_college < other_student_rank
                ):
                    envy_counts[student_id] += 1

    max_envy = max(envy_counts.values())
    return max_envy


def compare_algorithms():
    """Compare EF-k for different algorithms."""
    # Load synthetic files
    students_df = pd.read_csv('synthetic_students.csv')
    colleges_df = pd.read_csv('synthetic_universities.csv')

    students = [
        {
            'Student_ID': row['Student_ID'],
            'Preferences': list(map(int, row['Preferences'].split(',')))
        }
        for _, row in students_df.iterrows()
    ]

    colleges = [
        {
            'University_ID': row['University_ID'],
            'Slots': row['Slots']
        }
        for _, row in colleges_df.iterrows()
    ]

    # Load matchings
    results_path = 'matchings_results'
    algorithms = {
        'Serial Dictatorship': os.path.join(results_path, 'serial_dictatorship.txt'),
        'ACDA': os.path.join(results_path, 'acda.txt'),
        'Stable Matching': os.path.join(results_path, 'stable_matching.txt')
    }

    ef_k_scores = {}

    for algo, file_path in algorithms.items():
        matching = load_matching(file_path)
        ef_k_scores[algo] = calculate_ef_k(matching, students, colleges)

    return ef_k_scores


if __name__ == "__main__":
    scores = compare_algorithms()
    for algo, score in scores.items():
        print(f"{algo} EF-k: {score}")

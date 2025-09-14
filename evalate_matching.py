"""
Evaluation in different ways of matching in bipartite graph.

1. **Exponential Score Difference (e^{|M(u) - M(v)|})**:
   - Assigns exponentially higher penalties for larger rank differences between matched nodes.
   - A lower score indicates a fairer matching with smaller differences in preferences.

2. **Average Difference (|M(u) - M(v)| / |V1|)**:
   - Normalizes the rank differences by the size of the node set.
   - A lower score indicates a fairer matching where differences are minimized relative to the size of the set.

3. **Weighted Logarithmic Function (M(u)ln(M(u)) + M(v)ln(M(v)) + |M(u) - M(v)|)**:
   - Considers the logarithmic weighting of ranks combined with the rank differences.
   - A lower score indicates a matching that balances preferences and differences effectively.

For balanced and nuanced matchings that account for both rank importance and fairness, opt for Weighted Logarithmic Function.

"""

import os
import math
import pandas as pd


def load_matching(file_path):
    """Load a matching from a text file."""
    with open(file_path, 'r') as f:
        return eval(f.read())


def exponential_score_difference(matching, students):
    """Evaluate fairness using e^{|M(u) - M(v)|}."""
    scores = []
    for student in students:
        student_id = student['Student_ID']
        if student_id in matching:
            allocated_university = matching[student_id]
            try:
                rank = student['Preferences'].index(allocated_university) + 1
            except ValueError:
                rank = len(student['Preferences']) + 1
            scores.append(math.exp(rank))
    return scores


def average_difference(matching, students, v1_size):
    """Evaluate fairness using |M(u) - M(v)| / |V1|."""
    scores = []
    for student in students:
        student_id = student['Student_ID']
        if student_id in matching:
            allocated_university = matching[student_id]
            try:
                rank = student['Preferences'].index(allocated_university) + 1
            except ValueError:
                rank = len(student['Preferences']) + 1
            scores.append(rank / v1_size)
    return scores


def weighted_logarithmic_function(matching, students):
    """Evaluate fairness using M(u)ln(M(u)) + M(v)ln(M(v)) + |M(u) - M(v)|."""
    scores = []
    for student in students:
        student_id = student['Student_ID']
        if student_id in matching:
            allocated_university = matching[student_id]
            try:
                rank = student['Preferences'].index(allocated_university) + 1
            except ValueError:
                rank = len(student['Preferences']) + 1
            log_part = rank * math.log(rank)
            scores.append(log_part + rank)
    return scores


def evaluate_matchings(file_name):
    """Evaluate matchings using different evaluation functions."""
    # Load the dataset
    students_df = pd.read_csv('synthetic_students.csv')
    students = [
        {
            'Student_ID': row['Student_ID'],
            'Preferences': list(map(int, row['Preferences'].split(',')))
        }
        for _, row in students_df.iterrows()
    ]

    # Load the matching
    matching = load_matching(os.path.join('matchings_results', file_name))

    # Calculate scores
    v1_size = len(students)
    exp_scores = exponential_score_difference(matching, students)
    avg_scores = average_difference(matching, students, v1_size)
    log_scores = weighted_logarithmic_function(matching, students)

    # Return average scores for each evaluation
    return {
        'Exponential Score': sum(exp_scores) / len(exp_scores),
        'Average Difference': sum(avg_scores) / len(avg_scores),
        'Weighted Logarithmic': sum(log_scores) / len(log_scores)
    }


if __name__ == "__main__":
    """
    Change the name of the file_name to whatever matching you want to evaluate.
    """
    file_name = "stable_matching.txt"
    results = evaluate_matchings(file_name)
    print("Evaluation Results:", results)

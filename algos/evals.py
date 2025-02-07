"""
TODO:
- Vectorize functions since quadratic complexity.
- Deal with incomplete lists?
- sum evals
"""

from typing import Dict

from data.data_structures import College, Student


def is_envy_justified(student_id: int, other_id: int, assigned_college_id: int,
                      students: Dict[int, Student], colleges: Dict[int, College]) -> bool:
    """
    Checks wheteher a student has justified envy towards another student.
    As in Definition 2.5 in "Fairness and Efficiency Trade-off in Two-Sided Matching".

    Acceptable-ness always holds since we assume students prefer some college to none,
    so we don't check it.

    Parameters:
        student_id: The student who is envying
        other_id: The student who is envied
        assigned_college_id: The college assigned to student_id
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
    """

    student_pref = students[student_id]['preferences']
    other_pref = students[other_id]['preferences']
    college_pref = colleges[assigned_college_id]['preferences']

    student_prefers_over_other = student_pref.index(assigned_college_id) > other_pref.index(assigned_college_id) 
    college_prefers_other_over_student = college_pref.index(other_id) < college_pref.index(student_id)

    return student_prefers_over_other and college_prefers_other_over_student

def is_efk(students: Dict[int, Student], colleges: Dict[int, College], matching: Dict[int, int], k: int) -> bool:
    """
    Checks whether a matching is envy-free up to k peers.
    As in definition 5.1 in "Fairness and Efficiency Trade-off in Two-Sided Matching".

    Parameters:
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
        matching: A dictionary mapping student ids to college ids
        k: The number of peers to check for envy-freeness
    """

    for student_id in students:
        envy_peers = 0
        for other_id in students:

            if student_id == other_id:
                continue

            if is_envy_justified(student_id, other_id, matching[student_id], students, colleges):
                envy_peers += 1

            if envy_peers > k:
                return False
        
    return True

def calculate_efk(students: Dict[int, Student], colleges: Dict[int, College], matching: Dict[int, int]) -> int:
    """
    Calculates the maximum number of peers that some student has justified envy towards.
    This is the lower k for which `is_efk` holds
    As in definition 5.1 in "Fairness and Efficiency Trade-off in Two-Sided Matching".

    Parameters:
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
        matching: A dictionary mapping student ids to college ids
    """

    k_lower_bound = 0
    for student_id in students:
        envy_peers = 0
        for other_id in students:

            if student_id == other_id:
                continue

            if is_envy_justified(student_id, other_id, matching[student_id], students, colleges):
                envy_peers += 1

        if envy_peers > k_lower_bound:
            k_lower_bound = envy_peers

    return k_lower_bound


"""
TODO: maybe need to consider acceptableness explicitly.
"""

from typing import Dict, List

from data.data_structures import College, Student


def match_serial_dictatorship(students: Dict[int, Student], colleges: Dict[int, College], master_list: List[int]) -> Dict[int, int]:
    """
    Matches students to colleges using the Serial Dictatorship algorithm.
    As in section 3 in "Fairness and Efficiency Trade-off in Two-Sided Matching".
    
    Parameters:
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
        master_list: A list of student ids in the order of dictators

    Returns:
        A dictionary mapping student ids to college ids
    """

    matching = {}

    colleges_already_matched = {}

    ordered_students = {student_id: students[student_id] for student_id in master_list}
    for student_id, student in ordered_students.items():
        for college_id in student['preferences']:

            # We only check for capacity constraint
            if colleges_already_matched.get(college_id, 0) < colleges[college_id]['capacity']:
                matching[student_id] = college_id
                colleges_already_matched[college_id] = colleges_already_matched.get(college_id, 0) + 1
                break

    return matching

def match_acda(students: Dict[int, Student], colleges: Dict[int, College], quotas: List) -> Dict[int, int]: 
    """
    Matches students to colleges using the ACDA algorithm.
    As in section 3 in "Fairness and Efficiency Trade-off in Two-Sided Matching".
    
    Parameters:
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
    
    Returns:
        A dictionary mapping student ids to college ids
    """
    #artificial caps( max quotas)- vector q
    #run standard deferred acceptance mechanism
        #students pic their priority
        #college i admit to a waiting list q_i students depending on college preferences
        #repeat step 1 with next priority until every student is in cllege or rejected by all
    #from Gale and Shapley Stable Marriage paper
    waiting_lists = {}
    rejected_list = students
    round = 0

    while round < len(colleges) or not rejected_list:

        for student in rejected_list: #step 1
            waiting_lists[student[round]] = student
            rejected_list = []
        
        for college in waiting_lists: #step 2
            if len(waiting_lists[college]) > quotas[college]:

                ranked_students =  sorted(waiting_lists[college], key = lambda x: colleges[college].index(x))[:quotas[college]]
                waiting_lists[college] = ranked_students[:colleges[college]]
                rejected_list.extend(ranked_students[quotas[college]+1:])
                
                round +=1
    return waiting_lists
"""
This contains methods to synthetically generate preferences between students and colleges.
"""

from typing import Dict, List, Tuple

import numpy as np

from .data_structures import College, Student


def generate_preferences(num_students: int, num_colleges: int, min_capacity: int, max_capacity: int, phi_students: float = 0.5, phi_colleges: float = 0.5) -> Tuple[Dict[int, Student], Dict[int, College]]:
    """
    Generate random preferences between students and colleges.
    Use Mallow's model to generate both preference lists.
    Uniformly random capacities of colleges.
    
    Parameters:
        num_students: Number of students
        num_colleges: Number of colleges
        min_capacity: Minimum capacity of a college
        max_capacity: Maximum capacity of a college
        phi_students: Dispersion parameter for student preferences (0 < phi <= 1)
        phi_colleges: Dispersion parameter for college preferences (0 < phi <= 1)
    
    Returns:
        Lists of students and colleges as TypedDicts including preferences and capacities.
    """

    # generate student preferences
    students = {}
    for i in range(num_students):
        preferences = sample_mallows(num_colleges, phi_students)
        student = Student(id=i, preferences=preferences)
        students[i] = student

    # generate college preferences
    colleges = {}
    for i in range(num_colleges):
        capacity = np.random.randint(min_capacity, max_capacity + 1)
        preferences = sample_mallows(num_students, phi_colleges)
        college = College(id=i, capacity=capacity, preferences=preferences)
        colleges[i] = college

    return students, colleges


def sample_mallows(n: int, phi: float, master_ranking: List[int] | None = None) -> List[int]:
    """
    Generate a random ranking (preference list) of n items from the Mallows model with dispersion parameter phi,
    using the insertion algorithm.
    
    Parameters:
        n: Number of items to rank
        phi: Dispersion parameter (0 < phi <= 1).
        master_ranking: A master ranking to sample from. If None, we assume [0, 1, ..., n-1] as the master ranking.
    
    Returns:
        A list representing the sampled ranking, where 0th is the most preferred item.
    """

    # work with default master ranking [0, 1, ..., n-1]
    ranking = [] 
    for i in range(n):  
        insertion_positions = np.arange(len(ranking) + 1)

        probs = np.array([phi**j for j in range(len(ranking) + 1)])
        probs = probs / probs.sum()

        pos = np.random.choice(insertion_positions, p=probs)
        ranking.insert(pos, i)

    # permute elements to match master ranking if it is not [0, 1, ..., n-1]
    if master_ranking:
        ranking = [master_ranking[i] for i in ranking]
    
    return ranking
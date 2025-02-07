"""
This contains types to represent student and college preferences
and utility functions to save and load them from json.
"""

import json
from typing import Dict, List, Tuple, TypedDict


class Student(TypedDict):
    """
    Represents a student with preference list
    Attributes:
        id: int - id for student
        preferences: List[int] - list of college ids in order of preference, 0 being the most preferred
    """
    id: int 
    preferences: List[int] 

class College(TypedDict):
    """
    Represents a college with capacity and preference list
    Attributes:
        id: int - id for college
        capacity: int - number of students college can admit
        preferences: List[int] - list of student ids in order of preference, 0 being the most preferred
    """
    id: int
    capacity: int
    preferences: List[int]


## Utils to save and load data from json
def save_data_to_json(students: Dict[int, Student], colleges: Dict[int, College], filename: str):
    data = {
        'students': students,
        'colleges': colleges
    }
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_data_from_json(filename: str) -> Tuple[Dict[int, Student], Dict[int, College]]:
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['students'], data['colleges']



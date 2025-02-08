"""
This contains types to represent student and college preferences
and utility functions to save and load them from json.

We represent a single student as {id: int, preferences: List[int]} using TypedDict
So a new student is created with Student(id=1, preferences=[0, 1, 2])), but the created object will work just like a dictionary not a class.

A group of students, colleges would be
students = {1: Student(id=1, preferences=[0, 1, 2]), 2: Student(id=2, preferences=[1, 0, 2])}
where the ids are also the keys for fast lookup.

(the same for colleges)
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
    """
    Saves a dictionary of students and colleges to a json file

    Parameters:
        students: Dict[int, Student] - dictionary of students
        colleges: Dict[int, College] - dictionary of colleges
        filename: str - name of the file to save to
    """

    data = {
        'students': students,
        'colleges': colleges
    }
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_data_from_json(filename: str) -> Tuple[Dict[int, Student], Dict[int, College]]:
    """
    Loads a dictionary of students and colleges from a json file.

    Parameters:
        filename: str - name of the file to load from

    Returns:
        Tuple of students and colleges as dictionaries (Dict[int, Student], Dict[int, College])
    """

    with open(filename, 'r') as f:
        data = json.load(f)
    return data['students'], data['colleges']



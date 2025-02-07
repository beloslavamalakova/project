from typing import Dict

from data.data_structures import College, Student


def match_gale_shapely(students: Dict[int, Student], colleges: Dict[int, College], matching: Dict[int, int]) -> Dict[int, int]:
    """
    Matches students to colleges using the Gale-Shapely algorithm.
    
    Parameters:
        students: A dictionary mapping student ids to student dicts
        colleges: A dictionary mapping college ids to college dicts
        matching: A dictionary mapping student ids to college ids

    Returns:
        A dictionary mapping student ids to college ids
    """

    raise NotImplementedError
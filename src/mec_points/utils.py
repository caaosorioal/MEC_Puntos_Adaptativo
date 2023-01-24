import numpy as np
from typing import List, Tuple

def nearest_point_to_mouse(mouse_position : Tuple, points : List[Tuple], radius : float) -> Tuple:
    """
    Check if the mouse is near to a point
    """
    for point in points:
        if np.linalg.norm(np.array(mouse_position) - np.array(point)) <= radius:
            return point

    return None

def check_for_solutions(lines : List[Tuple], solutions_lines : List[Tuple]) -> Tuple:
    """
    Check if a line is a solution
    """
    solutions = []
    for line in lines:
        if is_solution(line, solutions_lines):
            solutions.append(line)
    
    return solutions

def is_solution(line : Tuple, solutions : List[Tuple]) -> bool:
    """
    Check if a line is a solution
    """
    for solution in solutions:
        if are_the_same_points(line, solution):
            return True

    return False

def are_the_same_points(point1 : Tuple, point2 : Tuple) -> bool:
    """
    Check if two points are the same
    """
    return sorted(point1) == sorted(point2)


#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes a list
input_list of floats as argument and returns their sum as a float.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.

    Returns:
        float: The sum of the numbers in the input list.
    """
    return sum(input_list)

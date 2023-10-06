#!/usr/bin/env python3
"""
Annotate the below function’s parameters and
return values with the appropriate types
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Calculate the length of each element in a list of strings and
    return a list of tuples.

    Args:
        lst (List[str]): A list of strings.

    Returns:
        List[Tuple[str, int]]: A list of tuples, where each tuple
        contains a string from the input list
        and its corresponding length as an integer.
    """
    return [(i, len(i)) for i in lst]

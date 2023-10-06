#!/usr/bin/env python3
"""
Write a type-annotated function to_kv that takes a string k and an int
OR float v as arguments and returns a tuple. The first element of the
tuple is the string k. The second element is the square of the
int/float v and should be annotated as a float.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the string k and the square of the int/float v.

    Args:
        k (str): A string.
        v (Union[int, float]): An integer or a float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square
        of v as a float.
    """
    return (k, float(v * v))

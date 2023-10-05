#!/usr/bin/env python3
"""
Write a type-annotated function floor which takes a
float n as argument and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """
    Compute the floor of a floating-point number.

    Args:
        n (float): The input floating-point number.

    Returns:
        int: The floor of the input number, as an integer.
    """
    return math.floor(n)

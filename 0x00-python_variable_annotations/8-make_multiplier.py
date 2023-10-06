#!/usr/bin/env python3
"""
Write a type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies
a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by the
    specified multiplier.

    Args:
        multiplier (float): The multiplier to be used in the created function.

    Returns:
        Callable[[float], float]: A function that takes a float and
        returns the result of multiplication.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function

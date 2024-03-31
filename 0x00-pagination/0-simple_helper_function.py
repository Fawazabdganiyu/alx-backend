#!/usr/bin/env python3
""" Definition of index_range helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return the start and end index corresponding to range of indexes
    to return in a list of the given parameters
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return start_index, end_index

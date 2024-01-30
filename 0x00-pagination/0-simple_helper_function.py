#!/usr/bin/env python3
''' a function named index_range that takes two integer arguments '''
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    ''' function should return a tuple of size two
        containing a start index and an end index '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)

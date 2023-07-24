#!/usr/bin/env python3
"""simple helper
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ index range

    Args:
        page (int): int param
        page_size (int): int param

    Returns:
        Tuple[int, int]: index range
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)

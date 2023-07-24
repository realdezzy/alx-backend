#!/usr/bin/env python3
"""Get page
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get data within a given range

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: list of data
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if end >= len(dataset):
            return []
        return dataset[start:end]

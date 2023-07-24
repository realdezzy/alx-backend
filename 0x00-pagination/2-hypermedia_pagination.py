#!/usr/bin/env python3
"""Hypermedia pagination"""
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
        """_summary_

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start, end = index_range(page, page_size)
        if end >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ Get pages in hypermedia format

        Args:
            page (int, optional): page number. Defaults to 1.
            page_size (int, optional): page size. Defaults to 10.

        Returns:
            dict: Returns a dictionary
        """
        data = self.get_page(page, page_size)
        total_size = math.ceil(len(self.__dataset) / page_size)
        previous_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_size else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': previous_page,
            'total_pages': total_size
            }

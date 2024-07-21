#!/usr/bin/env python3
"""
1-simple_pagination module
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size.
    The function should return a tuple of size two containing
    the start index and end index.
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

    def dataset(self) -> List[List[str]]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a page of the dataset with the specified page,
        number and page size."""
        # Check values
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        # Get dataset and index range
        data = self.dataset()
        start_index, end_index = index_range(page, page_size)

        # Handle out-of-bounds errors
        if start_index > len(data):
            return []

        # Paginate data
        paginated_items = data[start_index:end_index]
        return paginated_items

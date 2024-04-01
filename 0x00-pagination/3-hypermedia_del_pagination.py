#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a databse of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_available_index(self, index: int) -> int:
        """Get the next available index
        """
        if index in self.__indexed_dataset:
            return index

        return self.get_available_index(index + 1)

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia index of data in dataset
        """
        assert 0 <= index <= len(self.__indexed_dataset)
        current_index = self.get_available_index(index)
        next_index = current_index + page_size

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': [self.__indexed_dataset.get(i)
                     for i in range(current_index, next_index)]
        }

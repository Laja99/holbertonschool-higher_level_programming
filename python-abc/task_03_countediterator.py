#!/usr/bin/python3
"""
Module task_03_countediterator
Demonstrates subclassing of Python iterators and overriding __next__ to
track the number of items iterated.
"""


class CountedIterator:
    """
    An iterator wrapper that counts the number of items iterated over.

    Attributes:
        iterator (iterator): The underlying iterator object.
        count (int): Number of items returned so far.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator.

        Args:
            iterable (iterable): Any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the counter.

        Raises:
            StopIteration: When there are no more items to return.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items that have been iterated over so far.

        Returns:
            int: Number of items iterated.
        """
        return self.count

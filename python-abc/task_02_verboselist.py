#!/usr/bin/python3
"""
Module task_02_verboselist
Defines a VerboseList class that extends Python's built-in list.
It prints notifications whenever items are added or removed.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when items are added or removed.
    """

    def append(self, item):
        """
        Append an item to the list and print a message.

        Args:
            item: The item to add.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list by appending elements from
        the iterable and print a message.

        Args:
            iterable: An iterable of items to add.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of item from the list and print a message.

        Args:
            item: The item to remove.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return item at index (default last) and print a message.

        Args:
            index (int, optional): The index of the item to pop.

        Returns:
            The popped item.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

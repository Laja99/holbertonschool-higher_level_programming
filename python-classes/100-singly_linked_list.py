#!/usr/bin/python3
"""
Singly linked list module
"""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a node.

        Args:
            data (int): the value of the node
            next_node (Node, optional): reference to the next node (default None)

        Raises:
            TypeError: if data is not an integer or next_node is not a Node/None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data with validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node with validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node with value into the list at the correct sorted position.

        Args:
            value (int): value for the new Node
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        String representation of the list.
        Each node's data on a new line.
        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

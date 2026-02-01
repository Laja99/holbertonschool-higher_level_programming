#!/usr/bin/python3
"""
generation module for Python project
"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    return: JSON representation
    """
    return json.dumps(my_obj)

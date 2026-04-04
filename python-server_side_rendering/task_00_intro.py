#!/usr/bin/env python3
"""
Template invitation generator
"""

import os
import logging


def generate_invitations(template, attendees):
    """
    Generate invitation files from a template and list of attendees.

    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee data

    Returns:
        None
    """
    # Check input types
    if not isinstance(template, str):
        logging.error("Invalid input: template must be a string")
        return

    if not isinstance(attendees, list):
        logging.error("Invalid input: attendees must be a list")
        return

    # Check if attendees list contains dictionaries only
    if attendees and not all(isinstance(attendee, dict) for attendee in attendees):
        logging.error("Invalid input: attendees list must contain only dictionaries")
        return

    # Check for empty template
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        logging.error("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with values from attendee dictionary
            processed_content = template

            # Define expected placeholders
            placeholders = ['name', 'event_title', 'event_date', 'event_location']

            for placeholder in placeholders:
                value = attendee.get(placeholder, 'N/A')
                if value is None:
                    value = 'N/A'
                processed_content = processed_content.replace(
                    '{' + placeholder + '}', str(value)
                )

            # Generate output filename
            output_filename = f"output_{index}.txt"

            # Write to file
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(processed_content)

            print(f"Successfully created {output_filename}")

        except Exception as e:
            logging.error(f"Error processing attendee {index}: {str(e)}")
            continue


if __name__ == "__main__":
    # Example usage
    with open('template.txt', 'r') as file:
        template_content = file.read()

    attendees = [
        {"name": "Alice", "event_title": "Python Conference",
         "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop",
         "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit",
         "event_date": None, "event_location": "Boston"}
    ]

    generate_invitations(template_content, attendees)

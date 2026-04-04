#!/usr/bin/env python3
"""
Flask application with dynamic content using Jinja loops and conditions
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """
    Load items from items.json file

    Returns:
        list: List of items or empty list if file not found
    """
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('items', [])
    except FileNotFoundError:
        print("Error: items.json file not found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in items.json")
        return []


@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')


@app.route('/items')
def items_list():
    """Render the items page with dynamic list"""
    items = load_items()
    return render_template('items.html', items=items)


@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

#!/usr/bin/env python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def read_csv_file():
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return []
    except Exception:
        return []

def read_sqlite_db():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except Exception:
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if not source:
        return render_template('product_display.html',
                               error="Source parameter is required. Use ?source=json, ?source=csv, or ?source=sql")

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    elif source == 'sql':
        products = read_sqlite_db()
    else:
        return render_template('product_display.html',
                               error=f"Wrong source: '{source}'. Valid sources are 'json', 'csv', or 'sql'")

    if not products:
        return render_template('product_display.html',
                               error=f"No products found in {source} source or file is empty")

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = []
            for product in products:
                if product['id'] == product_id:
                    filtered_products.append(product)
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            return render_template('product_display.html', products=filtered_products)
        except ValueError:
            return render_template('product_display.html',
                                   error=f"Invalid id parameter: '{product_id}'. ID must be a number")

    return render_template('product_display.html', products=products)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

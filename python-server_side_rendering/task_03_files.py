#!/usr/bin/env python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json_file():
    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: products.json file not found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in products.json")
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
        print("Error: products.csv file not found")
        return []
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return []

def filter_product_by_id(products, product_id):
    return [product for product in products if product['id'] == product_id]

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if not source:
        return render_template('product_display.html',
                               error="Source parameter is required. Use ?source=json or ?source=csv")

    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        return render_template('product_display.html',
                               error=f"Wrong source: '{source}'. Valid sources are 'json' or 'csv'")

    if not products:
        return render_template('product_display.html',
                               error=f"No products found in {source} file or file is empty")

    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = filter_product_by_id(products, product_id)
            if not filtered_products:
                return render_template('product_display.html',
                                       error=f"Product with id {product_id} not found")
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

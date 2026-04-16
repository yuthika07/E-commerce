from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "ecommerce123securekey"

# Sample product data
PRODUCTS = [
    {'id': 1, 'name': 'Laptop', 'price': 999.99},
    {'id': 2, 'name': 'Mouse', 'price': 29.99},
    {'id': 3, 'name': 'Keyboard', 'price': 79.99},
    {'id': 4, 'name': 'Monitor', 'price': 299.99},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', products=PRODUCTS)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

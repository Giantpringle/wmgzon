from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wmgzon.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255))  # Assuming you're storing image URLs

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "image": self.image
        }


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(80), nullable=False)


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/products', methods=['GET'])
def display_products():
    query = request.args
    products = Product.query
    if 'search' in query:
        products = products.filter(Product.name.contains(query['search']))
    if 'category' in query:
        products = products.filter_by(category=query['category'])
    if 'price_min' in query:
        products = products.filter(Product.price >= float(query['price_min']))
    if 'price_max' in query:
        products = products.filter(Product.price <= float(query['price_max']))
    return jsonify([product.to_json() for product in products.all()])


@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        image=data.get('image', '')  # Handle image as an optional field
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully!'}), 201


@app.route('/update_product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get_or_404(product_id)
    product.name = data.get('name', product.name)
    product.description = data.get('description', product.description)
    product.price = data.get('price', product.price)
    product.category = data.get('category', product.category)
    product.image = data.get('image', product.image)
    db.session.commit()
    return jsonify({'message': 'Product updated successfully!'})


@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully!'})


@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()
    order = Order(user_id=data['user_id'], status='Processing')

    for item in data['cart_items']:
        product = Product.query.get(item['product_id'])
        if not product:
            return jsonify({'message': 'Product not found'}), 404
        order_item = OrderItem(order=order, product=product, quantity=item['quantity'])
        db.session.add(order_item)

    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Checkout successful', 'order_id': order.id}), 201


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

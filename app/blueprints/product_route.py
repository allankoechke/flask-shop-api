from flask import Blueprint, jsonify
from app.models.product import Product

products = Blueprint('products', __name__)

@products.route('/api/products')
def _products():
    return jsonify('Products')

@products.route('/api/products/<id>')
def _product(id):
    return jsonify(f'Specific product: {id}')
from flask import Blueprint, render_template, jsonify

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return jsonify('Hello World')
from typing import Any
from flask import Flask, g, current_app, request, jsonify, url_for, redirect, make_response
from werkzeug.routing import BaseConverter

# Create a Flask app
app = Flask(__name__)

# Class for custom list converter
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value) for value in values)

app.url_map.converters['list'] = ListConverter

# Set a global user for current request
@app.before_request
def before_request():
    g.user = "Guest"

# Define a route for the default URL
@app.route('/')
def index():
    return f'Hello, {g.user} from {current_app.name}'

# Define Dynamic URL
@app.route('/user/<int:user_id>')
def show_user_profile(user_id):
    return f'User ID: {user_id}'

# Access via /items/1,2,3
@app.route('/items/<list:items>')
def show_items(items):
    return f'Items: {items}'

# Building with url_for
@app.route('/')
def home():
    return redirect(url_for('show_user_profile', user_id=42))

# Using request attributes
@app.route('/data', methods=['POST'])
def handle_data():
    json_data = request.json
    return {'received': json_data}

# Customization of response
@app.route('/cookie')
def set_cookie():
    resp = make_response('Setting a cookie!')
    resp.set_cookie('flask_cookie', 'cookie_value')
    return resp



if __name__ == "__main__":
    app.run(debug=True)
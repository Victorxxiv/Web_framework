from typing import Any
from flask import Flask, g, current_app, request, jsonify, url_for, redirect
from flask import Flask, make_response, render_template
from werkzeug.routing import BaseConverter
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import DataRequired

# Create a Flask app
app = Flask(__name__)

# Class for custom list converter
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    
    def to_url(self, values):
        return ','.join(BaseConverter.to_url(value) for value in values)

app.url_map.converters['list'] = ListConverter

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Pasword', validators=[DataRequired()])
    submit = SubmitField('Submit')

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f'Welcome, {form.username.data}!'
    return render_template('login.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)
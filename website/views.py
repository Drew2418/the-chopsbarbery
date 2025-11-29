from flask import Blueprint, render_template

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/about')
def about():
    return render_template('about.html')

# You can add more pages later
@routes.route('/team')
def team():
    return render_template('team.html')

@routes.route('/services')
def services():
    return render_template('services.html')

@routes.route('/book')
def book():
    return render_template('book.html')

@routes.route('/contact')
def contact():
    return render_template('contact.html')

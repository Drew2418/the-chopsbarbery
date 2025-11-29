from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret1'

    from .views import routes  # Import the blueprint
    app.register_blueprint(routes)

    return app
from flask import Flask

# All blueprints
from .blueprints import home_route


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Initialize extensions, blueprints, etc.

    app.register_blueprint(home_route.home, url_prefix='/')

    return app
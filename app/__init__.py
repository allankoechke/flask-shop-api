from flask import Flask
from .extensions import db #, migrate

# All blueprints
from .blueprints import home_route, product_route


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    # migrate.init_app(app, db)

    # Initialize extensions, blueprints, etc.
    app.register_blueprint(home_route.home, url_prefix='/')
    app.register_blueprint(product_route.products, url_prefix='/')

    return app
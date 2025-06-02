from flask import Flask
from .config import Config
from .routes import api_blueprint
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi database
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(api_blueprint)

    return app

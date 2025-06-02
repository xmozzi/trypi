from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Inisialisasi objek db untuk SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load konfigurasi dari file config.py
    app.config.from_object(Config)

    # Inisialisasi db
    db.init_app(app)

    # Register blueprint (routes)
    from .routes import main
    app.register_blueprint(main)

    return app

from flask import Flask
from .config import Config
from .models import db
from .routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi database
    db.init_app(app)

    # Register blueprint untuk routes
    app.register_blueprint(main_bp)

    return app

from flask import Blueprint, jsonify
from .models import User, UserSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "Hello, Flask! Welcome to your first API."

@main_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    return jsonify(user_schema.dump(users))

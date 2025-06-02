from flask import Blueprint, request, jsonify
from .controllers import create_user, get_all_users, get_user_by_id, update_user, delete_user
from .schemas import UserSchema

api_blueprint = Blueprint('api', __name__)

# Rute untuk menambah user
@api_blueprint.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Missing data"}), 400
    user = create_user(data)
    user_schema = UserSchema()
    return user_schema.jsonify(user), 201

# Rute untuk mendapatkan semua users
@api_blueprint.route('/api/users', methods=['GET'])
def get_users():
    users = get_all_users()
    user_schema = UserSchema(many=True)
    return user_schema.jsonify(users)

# Rute untuk mendapatkan user berdasarkan ID
@api_blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        user_schema = UserSchema()
        return user_schema.jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Rute untuk memperbarui user berdasarkan ID
@api_blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data:
        return jsonify({"error": "Missing data"}), 400
    user = update_user(user_id, data)
    if user:
        user_schema = UserSchema()
        return user_schema.jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Rute untuk menghapus user berdasarkan ID
@api_blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    user = delete_user(user_id)
    if user:
        return jsonify({"message": "User deleted successfully"}), 200
    return jsonify({"error": "User not found"}), 404

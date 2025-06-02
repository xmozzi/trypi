from flask import Flask, jsonify, request
from functools import wraps

app = Flask(__name__)

# Data Dummy (Database Sederhana)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    {"id": 3, "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": 4, "name": "Bob Lee", "email": "bob@example.com"},
]

# Dummy Authenticator for Demonstration (Can be improved with JWT or OAuth)
def check_auth(username, password):
    return username == "admin" and password == "secret"

def requires_auth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({"error": "Authentication required"}), 401
        return f(*args, **kwargs)
    return decorated_function

# Halaman Utama
@app.route('/')
def home():
    return "Hello, Flask! This is your first API."

# Route untuk mendapatkan semua pengguna
@app.route('/users', methods=['GET'])
@requires_auth
def get_users():
    return jsonify(users)

# Route untuk mendapatkan satu pengguna berdasarkan ID
@app.route('/users/<int:user_id>', methods=['GET'])
@requires_auth
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Route untuk menambah pengguna baru
@app.route('/users', methods=['POST'])
@requires_auth
def add_user():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Missing required fields"}), 400
    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Route untuk mengupdate data pengguna
@app.route('/users/<int:user_id>', methods=['PUT'])
@requires_auth
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])
    return jsonify(user)

# Route untuk menghapus pengguna berdasarkan ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
@requires_auth
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

# Search Users berdasarkan nama
@app.route('/users/search', methods=['GET'])
@requires_auth
def search_users():
    query = request.args.get('name', '')
    filtered_users = [user for user in users if query.lower() in user["name"].lower()]
    return jsonify(filtered_users)

# Sort Users berdasarkan nama atau email
@app.route('/users/sort', methods=['GET'])
@requires_auth
def sort_users():
    sort_by = request.args.get('sort_by', 'name')
    if sort_by not in ['name', 'email']:
        return jsonify({"error": "Invalid sort parameter"}), 400
    sorted_users = sorted(users, key=lambda x: x[sort_by].lower())
    return jsonify(sorted_users)

# Paginate Users (Limit dan Offset)
@app.route('/users/paginate', methods=['GET'])
@requires_auth
def paginate_users():
    try:
        limit = int(request.args.get('limit', 2))  # default 2 users per page
        offset = int(request.args.get('offset', 0))  # default start from first user
    except ValueError:
        return jsonify({"error": "Invalid limit or offset"}), 400

    paginated_users = users[offset:offset + limit]
    return jsonify(paginated_users)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "up"}), 200

# Error Handling untuk 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

# Error Handling untuk 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

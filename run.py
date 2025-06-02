from flask import Flask, jsonify, request

app = Flask(__name__)

# Data Dummy (Database Sederhana)
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]

# Halaman Utama
@app.route('/')
def home():
    return "Hello, Flask! This is your first API."

# Route untuk mendapatkan semua pengguna
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route untuk mendapatkan satu pengguna berdasarkan ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# Route untuk menambah pengguna baru
@app.route('/users', methods=['POST'])
def add_user():
    # Ambil data dari request JSON
    data = request.get_json()

    # Validasi data
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({"error": "Missing required fields"}), 400

    # Buat pengguna baru
    new_user = {
        "id": len(users) + 1,
        "name": data['name'],
        "email": data['email']
    }

    # Tambahkan ke daftar pengguna
    users.append(new_user)
    return jsonify(new_user), 201

# Route untuk mengupdate data pengguna
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    # Ambil data baru dari request
    data = request.get_json()

    # Update data pengguna
    user['name'] = data.get('name', user['name'])
    user['email'] = data.get('email', user['email'])

    return jsonify(user)

# Route untuk menghapus pengguna berdasarkan ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return jsonify({"message": "User deleted successfully"}), 200

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

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Welcome to your first API."

@app.route('/api', methods=['GET'])
def api():
    data = {
        "message": "Welcome to your Flask API!",
        "status": "success"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

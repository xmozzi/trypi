from flask import Blueprint, jsonify, request
from .models import db, User, Post

main = Blueprint('main', __name__)

# Route untuk home page
@main.route('/')
def home():
    return "Welcome to the Flask API!"

# Route untuk mendapatkan semua user
@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    return jsonify(users_list)

# Route untuk membuat user baru
@main.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

# Route untuk mendapatkan semua posts
@main.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    posts_list = []
    for post in posts:
        posts_list.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'user_id': post.user_id
        })
    return jsonify(posts_list)

# Route untuk membuat post baru
@main.route('/post', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({"message": "Post created!"}), 201

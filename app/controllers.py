from .models import db, User
from .schemas import UserSchema

def create_user(data):
    user = User(name=data['name'], age=data['age'])
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    users = User.query.all()
    return users

def get_user_by_id(user_id):
    return User.query.get(user_id)

def update_user(user_id, data):
    user = User.query.get(user_id)
    if user:
        user.name = data['name']
        user.age = data['age']
        db.session.commit()
        return user
    return None

def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return user
    return None

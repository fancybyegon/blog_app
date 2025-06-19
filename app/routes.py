from flask import Blueprint, request, jsonify
from .models import db, User, Post, Comment

api = Blueprint('api', __name__)

# USERS
@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = User(username=data['username'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# POSTS
@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts]), 200

@api.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict()), 200

@api.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    try:
        post = Post(
            title=data['title'],
            content=data['content'],
            user_id=data['user_id']
        )
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/posts/<int:id>', methods=['PATCH'])
def update_post(id):
    post = Post.query.get_or_404(id)
    data = request.get_json()
    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']
    db.session.commit()
    return jsonify(post.to_dict()), 200

@api.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return '', 204

# COMMENTS
@api.route('/comments', methods=['POST'])
def create_comment():
    data = request.get_json()
    try:
        comment = Comment(
            content=data['content'],
            user_id=data['user_id'],
            post_id=data['post_id']
        )
        db.session.add(comment)
        db.session.commit()
        return jsonify(comment.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

from . import db
from sqlalchemy.orm import validates

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)

    @validates('username')
    def validate_username(self, key, username):
        assert username.strip() != '', 'Username cannot be empty'
        return username

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "posts": [post.to_dict_simple() for post in self.posts]
        }

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    @validates('title')
    def validate_title(self, key, title):
        assert title.strip() != '', 'Title cannot be empty'
        return title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "author": {
                "id": self.author.id,
                "username": self.author.username
            },
            "comments": [comment.to_dict() for comment in self.comments]
        }

    def to_dict_simple(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    @validates('content')
    def validate_content(self, key, content):
        assert content.strip() != '', 'Content cannot be empty'
        return content

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "user": {
                "id": self.user.id,
                "username": self.user.username
            },
            "post_id": self.post_id
        }

from datetime import datetime
from flask_login import UserMixin,current_user
from werkzeug.security import generate_password_hash,check_password_hash
from app import db,login_manager


      #user authentication
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),nullable=False,unique=True)
    email = db.Column(db.String(255),nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        db.session.generate_password_hash(password)
        self.password = pass_hash

    def check_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self):
        return f'User: {self.username}'


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String, nullable=False)
    post = db.Column(db.String,nullable=False)
    comment = db.relationship('Comment', backref='post', lazy='dynamic')
    category = db.Column(db.String,nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    up_vote = db.relationship('Upvote',backref='post', lazy='dynamic')
    down_vote = db.relationship('DownVote', backref='post', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Post Title: {self.title}'

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'),nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return comments

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls,id):
        upvote_post = Upvote(user=current_user,post_id=id)
        upvote_post.save()

    @classmethod
    def query_upvotes(cls,id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes
    
    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'


class DownVote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls,id):
        downvote_post = DownVote(user=current_user,post_id=id)
        downvote_post.save()
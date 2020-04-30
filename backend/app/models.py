from app import db

from datetime import datetime

class User(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), default='anonymous')
    todos   = db.relationship('Todo', backref='author', lazy='dynamic')

class Todo(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    content         = db.Column(db.String(200), nullable=False)
    date_created    = db.Column(db.DateTime, default=datetime.now)
    owner           = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Task %r>' % self.id

# run this once to create all dbs!
# dont use it at all if you use flask-migrate!
# db.create_all()

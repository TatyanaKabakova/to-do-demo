from datetime import datetime
from app import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='to_do_list', lazy='dynamic')

    def __repr__(self):
        return '<TodoList {}>'.format(self.title)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text())
    todo_list_id = db.Column(db.Integer, db.ForeignKey('todo_list.id'))
    is_finished = db.Column(db.Boolean, default=False, server_default="false", nullable=False)

    def __repr__(self):
        return '<Task {}>'.format(self.body)

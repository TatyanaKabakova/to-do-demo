from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Create ToDo')


class TaskForm(FlaskForm):
    body = TextField('Body', validators=[DataRequired()])
    is_finished = BooleanField('Finished')
    submit = SubmitField('Submit')

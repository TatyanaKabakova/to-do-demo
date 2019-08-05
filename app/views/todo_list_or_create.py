from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import db
from app.forms import TodoForm, TaskForm
from app.models import TodoList, Task

todo_list_create = Blueprint('todo_list_or_create', __name__)


@todo_list_create.route('/', methods=['GET', 'POST'])
def todo_list_or_create():
    todo_form = TodoForm()
    if todo_form.validate_on_submit():
        to_do_item = TodoList(title=todo_form.title.data)
        db.session.add(to_do_item)
        db.session.commit()
        return redirect(url_for('todo_list_or_create.todo_list_or_create'))
    to_do_list = TodoList.query.all()
    return render_template('to_do_list.html', form=todo_form, todo_list=to_do_list)

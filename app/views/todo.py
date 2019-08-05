from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import db
from app.forms import TodoForm, TaskForm
from app.models import TodoList, Task

todo_item = Blueprint('todo', __name__)


@todo_item.route('/', methods=['GET', 'POST'])
def todo_list_or_create():
    todo_form = TodoForm()
    if todo_form.validate_on_submit():
        to_do_item = TodoList(title=todo_form.title.data)
        db.session.add(to_do_item)
        db.session.commit()
        return redirect(url_for('todo.todo_list_or_create'))
    to_do_list = TodoList.query.all()
    return render_template('to_do_list.html', form=todo_form, todo_list=to_do_list)


@todo_item.route('/<todo_id>', methods=['GET',])
def task_list(todo_id):
    task_form = TaskForm()
    todo_object = TodoList.query.filter_by(id=todo_id).first_or_404()
    tasks = Task.query.filter_by(todo_list_id=todo_id).order_by(Task.is_finished)
    return render_template('tasks_list.html', form=task_form, todo_item=todo_object, tasks=tasks)

from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import app, db
from app.forms import TodoForm, TaskForm
from app.models import TodoList, Task

task_list_create = Blueprint('task_list_or_create', __name__)


@task_list_create.route('/todo/<todo_id>', methods=['GET', 'POST'])
def task_list_or_create(todo_id):
    task_form = TaskForm()
    if task_form.validate_on_submit():
        task_item = Task(body=task_form.body.data, todo_list_id=todo_id)
        db.session.add(task_item)
        db.session.commit()
        return redirect(url_for('task_list_or_create.task_list_or_create', todo_id=todo_id))
    todo_item = TodoList.query.filter_by(id=todo_id).first_or_404()
    tasks = Task.query.filter_by(todo_list_id=todo_id).order_by(Task.is_finished)
    return render_template('tasks_list.html', form=task_form, todo_item=todo_item, tasks=tasks)

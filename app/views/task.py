from flask import render_template, redirect, url_for, Blueprint
from app import db
from app.forms import TaskForm
from app.models import TodoList, Task

task_item = Blueprint('task', __name__)


@task_item.route('/edit/<task_id>', methods=['GET', 'POST'])
def task_edit(task_id):
    task_object = Task.query.filter_by(id=task_id).first_or_404()
    task_form = TaskForm(body=task_object.body, is_finished=task_object.is_finished)
    if task_form.validate_on_submit():
        task_object.body = task_form.body.data
        task_object.is_finished = task_form.is_finished.data
        db.session.commit()
        return redirect(url_for('todo.task_list', todo_id=task_object.todo_list_id))
    todo_item = TodoList.query.filter_by(id=task_object.todo_list_id).first_or_404()
    return render_template('task_item.html', form=task_form, todo_item=todo_item, task=task_object)


@task_item.route('/delete/<task_id>', methods=['GET', ])
def task_delete(task_id):
    task_object = Task.query.filter_by(id=task_id).first_or_404()
    todo_list_id = task_object.todo_list_id
    db.session.delete(task_object)
    db.session.commit()
    return redirect(url_for('todo.task_list', todo_id=todo_list_id))


@task_item.route('/<todo_id>', methods=['POST', ])
def task_create(todo_id):
    task_form = TaskForm()
    if task_form.validate_on_submit():
        task_object = Task(body=task_form.body.data, todo_list_id=todo_id)
        db.session.add(task_object)
        db.session.commit()
        return redirect(url_for('todo.task_list', todo_id=todo_id))
    todo_item = TodoList.query.filter_by(id=todo_id).first_or_404()
    tasks = Task.query.filter_by(todo_list_id=todo_id).order_by(Task.is_finished)
    return render_template('tasks_list.html', form=task_form, todo_item=todo_item, tasks=tasks)

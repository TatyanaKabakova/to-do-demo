from flask import render_template, flash, redirect, url_for, request, Blueprint
from app import app, db
from app.forms import TodoForm, TaskForm
from app.models import TodoList, Task

task_item_edit = Blueprint('task_edit', __name__)


@task_item_edit.route('/task/<task_id>', methods=['GET', 'POST'])
def task_edit(task_id):
    task_item = Task.query.filter_by(id=task_id).first_or_404()
    print("is_finished=task_item.is_finished", task_item.is_finished)
    task_form = TaskForm(body=task_item.body, is_finished=task_item.is_finished)
    if task_form.validate_on_submit():
        task_item.body = task_form.body.data
        task_item.is_finished = task_form.is_finished.data
        db.session.commit()
        return redirect(url_for('task_list_or_create.task_list_or_create', todo_id=task_item.todo_list_id))
    todo_item = TodoList.query.filter_by(id=task_item.todo_list_id).first_or_404()
    return render_template('task_item.html', form=task_form, todo_item=todo_item, task=task_item)
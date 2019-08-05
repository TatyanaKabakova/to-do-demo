from flask import redirect, url_for, Blueprint
from app import db
from app.models import Task

task_item_delete = Blueprint('task_delete', __name__)


@task_item_delete.route('/task/delete/<task_id>', methods=['GET', ])
def task_delete(task_id):
    task_item = Task.query.filter_by(id=task_id).first_or_404()
    todo_list_id = task_item.todo_list_id
    db.session.delete(task_item)
    db.session.commit()
    return redirect(url_for('task_list_or_create.task_list_or_create', todo_id=todo_list_id))

from flask import Flask

from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views.todo_list_or_create import todo_list_create
from .views.task_list_or_create import task_list_create
from .views.task_delete import task_item_delete
from .views.task_edit import task_item_edit

app.register_blueprint(todo_list_create)
app.register_blueprint(task_list_create)
app.register_blueprint(task_item_delete)
app.register_blueprint(task_item_edit)

from app import models


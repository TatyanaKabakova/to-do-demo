from flask import Flask

from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .views.todo import todo_item
from .views.task import task_item

app.register_blueprint(todo_item, url_prefix='/todo/')
app.register_blueprint(task_item, url_prefix='/task/')

from app import models


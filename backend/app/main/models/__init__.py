from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .UserModel import UserModel
from .AdminModel import AdminModel
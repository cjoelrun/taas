from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Base = declarative_base()


class Model(db.Model, Base):
    __abstract__ = True

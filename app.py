from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app(): # Creating function so that file does not gets auto-executed while importing
    app = Flask(__name__, template_folder="templates")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trip_data.db"
    db.init_app(app)

    migrate = Migrate(app, db)
    return app
    
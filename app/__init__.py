from flask import Flask

from app.core.routes import core_blueprint
from app.extensions import db, migrate


def register_blueprint(app):
    app.register_blueprint(core_blueprint)


app = Flask(__name__)
register_blueprint(app)

app.config.from_object("configs.ConfigDev")


db.init_app(app)
migrate.init_app(app, db)

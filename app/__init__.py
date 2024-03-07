from flask import Flask

from app.extensions import db, migrate
from app.core.routes import core_blueprint


def register_blueprint(app):
    app.register_blueprint(core_blueprint)




app = Flask(__name__)
app.config.from_object('configs.ConfigDev')

register_blueprint(app)


db.init_app(app)
migrate.init_app(app)
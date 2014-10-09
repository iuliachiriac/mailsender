from flask import Flask


def create_app(config=None):
    app = Flask(__name__)
    if config:
        app.config.from_pyfile(config)

    return app

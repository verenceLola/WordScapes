from flask import Flask


def create_app():
    app = Flask('__name__')

    from .routes import bp
    app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='index')

    return app

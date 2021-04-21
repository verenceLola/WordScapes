from flask import Flask, jsonify


def create_app():
    app = Flask("__name__")

    from .routes import bp

    app.register_blueprint(bp)
    # app.add_url_rule("/", endpoint="index")

    @app.errorhandler(404)
    def not_found(e):
        """custom error handler for 404 Not Found Error"""
        return (
            jsonify({"error": "Not Found. Please refer to the API documentation"}),
            404,
        )

    @app.errorhandler(500)
    def server_error(e):
        """custom error handler for 500 Internal Sever Error"""
        app.logger.error("An error occured", e)
        return jsonify({"error": "An error occured. Please try again later"}), 500

    @app.errorhandler(405)
    def not_implemented(e):
        """custom error handler for 405 Not Implemented Error"""
        return (
            jsonify(
                {"error": "Method not implemented. Refer to the API documentation"}
            ),
            405,
        )

    return app

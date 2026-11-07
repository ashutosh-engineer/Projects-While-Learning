from flask import Flask
from config.config import  DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app=Flask(__name__)
    app.config.from_object(config_class)
    from routes.posts import post_bp
    from routes.auth import auth_bp
    from routes.comments import comments_bp

    app.register_blueprint(post_bp, url_prefix= "/api/posts")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(comments_bp, url_prefix="/api/comments")
    # print(app.config["SECRET_KEY"])
    # print(app.config["APP_NAME"])

    @app.errorhandler(404)
    def does_not_exist(error):
        return {
            "error" : "Post not found",
            "status" : 404
        }, 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return {
            "error" : "method not allowed",
            "status code" : 405
        }, 405

    @app.errorhandler(500)
    def handle_internal_server(error):
        return {
            "error" : "Internal server Error",
            "status" : 500
        }, 500

    return app


if __name__ == "__main__":
    app=create_app()
    app.run()

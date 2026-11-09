from flask import Flask, current_app , g 
from config.config import  DevelopmentConfig
import uuid
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.utils import get_remote_address


def create_app(config_class=DevelopmentConfig):
    app=Flask(__name__)
    limiter = Limiter(key_func = get_remote_address, app=app, default_limits=["3 per minute"])
    app.config.from_object(config_class)
    if app.config["DEBUG"]:
        Talisman(
            app,
            force_https=False,
            strict_transport_security=False
        )
    else:
        Talisman(app)


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
            "error" : "Not found",
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

    @app.before_request
    def give_request_id():
        g.request_id= str(uuid.uuid4())
            
    @app.after_request
    def add_request_id_header(response):
        response.headers["X-Request-ID"] =g.request_id
        return response
    
    @app.teardown_request
    def cleanup_request(exception):
        if exception:
            print(f"Request failed: {exception}")

    return app


if __name__ == "__main__":
    app=create_app()

    app.run()

from flask import Flask


def create_app(config_name = "Developement"):
    app=Flask(__name__)

    from routes.posts import post_bp
    from routes.auth import auth_bp
    from routes.comments import coment_bp

    app.register_blueprint(post_bp, url_prefix= "/api/posts")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(coment_bp, url_prefix="/api/comments")


    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug = True)

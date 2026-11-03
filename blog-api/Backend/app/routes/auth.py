from flask import Blueprint

auth_bp= Blueprint("authentication" , __name__)


@auth_bp.route("/authentication", methods=["GET", "POST"])
def authenticate_user():
    pass


@auth_bp.route("/authorization", methods=["GET", "POST"])
def authorize_users():
    pass

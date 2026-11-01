from flask import Blueprint

auth_bp= Blueprint("Authentication" , __name__)


@auth_bp.route("/authentication" , method= ["GET" , "POST"])
def authenticate_user():
    pass


@auth_bp.route("Authorization" , method=["GET" , "POST"])
def authrize_users():
    pass


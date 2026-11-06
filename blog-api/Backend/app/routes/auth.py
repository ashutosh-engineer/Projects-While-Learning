from flask import Blueprint , jsonify

auth_bp= Blueprint("authentication" , __name__)


@auth_bp.route("/authentication", methods=["POST"])
def authenticate_user():
      return jsonify({
            "error" : "Post is empety",
            "status" : 200
        }), 200


@auth_bp.route("/authorization", methods=["POST"])
def authorize_users():
      return jsonify({
            "error" : "Post is empety",
            "status" : 200
        }), 200

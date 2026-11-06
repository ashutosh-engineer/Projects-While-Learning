from flask import Blueprint , jsonify

comments_bp=Blueprint("commentsts" , __name__)


@comments_bp.route("/comments")
def  all_listed_comments():
    return jsonify({
          "error" : "Post is empety",
          "status" : 404
      }), 404


@comments_bp.route("/")
def make_comment():
      return jsonify({
            "error" : "Post is empety",
            "status" : 404
        }), 404


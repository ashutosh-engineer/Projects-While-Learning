from flask import Blueprint

comments_bp=Blueprint("commentsts" , __name__)


@comments_bp.route("/comments")
def  all_listed_comments():
    return "This all Listed comments"


@comments_bp.route("/")
def make_coment():
    pass


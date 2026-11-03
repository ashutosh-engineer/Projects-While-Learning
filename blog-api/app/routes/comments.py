from flask import Blueprint

comments_bp=Blueprint("commnets" , __name__)


@comments_bp.route("/Comments")
def  all_listed_comments():
    return "This all Listed comments"


@comments_bp.route("/")
def make_coment():
    pass


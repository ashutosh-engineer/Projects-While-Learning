from flask import Blueprint

coment_bp=Blueprint("Commnets" , __name__)


@coment_bp.route("/Comments")
def  all_listed_comments():
    return "This all Listed comments"


@coment_bp.route("/make_coment")
def make_coment():
    pass


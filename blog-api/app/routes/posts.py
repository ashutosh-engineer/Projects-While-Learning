from flask import Blueprint

post_bp= Blueprint("user" , __name__)

@post_bp.route("/posts")
def show_post():
    return "All the posts will be lsited here"



@post_bp.route("/write-post")
def write_post():
    pass





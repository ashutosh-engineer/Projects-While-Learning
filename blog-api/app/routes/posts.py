from flask import Blueprint , jsonify

post_bp= Blueprint("user" , __name__)

posts=[
    {
       "id": 1,
        "title": "Learning Flask",
        "content": "My first Flask post",
        "category": "python" 
    }
]

@post_bp.route("/" , methods=["GET"])
def show_post():
    if posts:
        return jsonify(posts), 200

    return jsonify({"error " : "No post found"}), 404


@post_bp.route("/<int:post_id>" , methods= ["GET"])
def specific_post(post_id):
    for post in posts:
        if post["id"] == post_id:
            return jsonify(post), 200

    return jsonify({"error" : "Post not found"}), 404


@post_bp.route("/category/<category_name>" , methods=["GET"])
def filter_posts(category_name):
    result=[]
    for pos in posts:
        if pos["category"] == category_name:
            result.append(pos)

    if result:
        return jsonify(result),200

    return jsonify({"error" : "Post not found"}) , 404




    





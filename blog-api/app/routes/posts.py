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

@post_bp.route("/posts" , methods=["GET"])
def show_post():
    if posts:
        return jsonify(posts), 200

    return jsonify({"Error " : "No post found"}), 404


@post_bp.route("/post/<int:id>" , methods= ["GET"])
def specific_post(id):
    for post in posts:
        if post["id"] == id:
            return jsonify({posts}), 200

    return jsonify({"Error" : "Post not found"}), 404


@post_bp.route("/filter/<category_name>" , methods=["GET"])
def filter(category_name):
    result=[]
    for pos in posts:
        if pos["category"] == category_name:
            result.append(pos)

        if result:
            return jsonify(result),200

    return jsonify({"Error" : "Unmatching Details"})




    





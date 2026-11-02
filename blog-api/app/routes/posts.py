from flask import Blueprint , jsonify , request

post_bp= Blueprint("user" , __name__)

posts=[
    {
       "id": 1,
        "title": "Learning Flask",
        "content": "My first Flask post",
        "category": "python" 
    }
]

@post_bp.route("/" , methods= ["POST"])
def post() ->dict:
    data=request.get_json(silent=True)
    if not isinstance(data, dict):
        return {"error" : "Valid json object needed"}, 400
    
    new_id=len(posts)+1
    title=data.get("title")
    content=data.get("content")
    category=data.get("category")

    if id is None:
        return{"error" : "id not generated"}, 400
    if title is None:
        return {"error" : "title is Required"}, 400

    if content is None:
        return {"error" : "Content is Required for posts"}, 400

    if category is None:
        return {"error" : "Category is needed to register the post"}, 400

    # Append the post in the list
    new_post= {
        "id" : id,
        "title" : title,
        "content" : content,
        "category" : category
    }

    posts.append(new_post)
    return jsonify(new_post), 201



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




    





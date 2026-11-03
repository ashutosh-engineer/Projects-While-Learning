from flask import Blueprint , jsonify , request

post_bp= Blueprint("posts" , __name__)

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

    if title is None:
        return {"error" : "title is Required"}, 400

    if content is None:
        return {"error" : "Content is Required for posts"}, 400

    if category is None:
        return {"error" : "Category is needed to register the post"}, 400

    # Append the post in the list
    new_post= {
        "id" : new_id,
        "title" : title,
        "content" : content,
        "category" : category
    }

    posts.append(new_post)
    return jsonify(new_post), 201

@post_bp.route("/<int:post_id>" , methods=["PUT"])
def change_content(post_id):
    data=request.get_json(silent= True)

    if not isinstance(data, dict):
        return {"error" : "Invalid data object not Json"},400

    
    new_title : str=data.get("title")
    new_content : str=data.get("content")
    new_category : str=data.get("category")

    # Validation
    if new_title is None:
        return {"error" : "title must be given"}, 400

    if new_content is None:
        return {"error" : "new Content must be Given"}, 400

    if new_category is None:
        return {"error": "Category must be Given"}, 400

    # Now as per the id update the reminaing data in the feilds

    for post in posts:
        if post["id"] == post_id:
            post["title"]=new_title
            post["content"]=new_content
            post["category"]=new_category

            return jsonify(post), 200

    return jsonify ({
        "ok" : "Post ost not found",
    }), 404


@post_bp.route("/<int:post_id>", methods=["PATCH"])
def change_partially(post_id):
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return {"error": "Valid JSON object is required"}, 400

    if not data:
        return {"error": "At least one field is required"}, 400

    for post in posts:
        if post["id"] == post_id:
            post["title"] = data.get("title", post["title"])
            post["content"] = data.get("content", post["content"])
            post["category"] = data.get("category", post["category"])

            return jsonify({
                "message": "Post updated successfully",
                "post": post
            }), 200

    return {"error": "Post not found"}, 404

#Read with URL Querry parameter
@post_bp.route("/" , methods=["GET"])
def show_post():
    category=request.args.get("category")

    if category is None:
        return jsonify(posts), 200

    result=[]

    for post in posts:
        if post["category"] == category:
            result.append(post)
            return jsonify(result), 200

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


#To delete the post
@post_bp.route("/<int:post_id>", methods=["DELETE"])
def delete(post_id):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)

            return "", 204


    return jsonify({"Error" : "Post not found"}), 404




    





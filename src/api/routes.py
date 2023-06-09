from flask import Blueprint, request, jsonify
from api.models import db, Post, Image, User
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from cloudinary import uploader

api = Blueprint('api', __name__)

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    post_dictionaries = [post.serialize() for post in posts]
    return jsonify(post_dictionaries)

@api.route('/posts', methods=['POST'])
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    request_body = request.get_json()
    new_post = Post(
        description=request_body["description"],
        location=request_body["location"],
        date=request_body["date"],
        user_id=user_id
    )
    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.serialize()), 201

@api.route("/post-images", methods=["POST"])
@jwt_required()
def create_post_image():
    image = request.files['file']
    post_id = request.form.get("post_id")
    response = uploader.upload(
        image,
        resource_type="image",
        folder="posts"
    )
    new_post_image = Image(
        post_id=post_id,
        url=response["secure_url"],
        public_id=response["public_id"]
    )
    db.session.add(new_post_image)
    db.session.commit()

    return jsonify(new_post_image.serialize()), 201

@api.route("/log-in", methods=["POST"])
def log_in():
    body = request.json
    user = User.query.filter_by(email=body["email"]).one_or_none()
    if user is None or not user.check_password(body["password"]):
        return "Invalid credentials", 401

    token = create_access_token(identity=user.id)
    return jsonify({
        "user": user.serialize(),
        "token": token
    }), 200

@api.route("/sign-up", methods=["POST"])
def sign_up():
    body = request.json
    user = User(
        email=body["email"],
        password=body["password"],
        name=body["name"]
    )
    db.session.add(user)
    db.session.commit()

    return jsonify(user.serialize()), 201



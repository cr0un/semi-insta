import logging

from flask import Blueprint, request, jsonify
from app.posts.DAO.postsDAO import postsDAO
from app.posts.DAO.commentsDAO import commentsDAO

api_blueprint = Blueprint('api_blueprint', __name__)

postsDAO = postsDAO("data/posts.json")
commentsDAO = commentsDAO("data/comments.json")

logger = logging.getLogger("basic")

@api_blueprint.route('/api/posts/')
def posts_all():
    logger.debug("Запрошены посты через api")
    posts = postsDAO.get_all()
    return jsonify(posts)

@api_blueprint.route('/api/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f"Запрошен пост по {post_pk} через api")
    post = postsDAO.get_by_pk(post_pk)
    return jsonify(post)

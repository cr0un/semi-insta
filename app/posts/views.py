import logging
from json import JSONDecodeError
from flask import Blueprint, render_template, request, abort
from app.posts.DAO.postsDAO import postsDAO
from app.posts.DAO.commentsDAO import commentsDAO


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
postsDAO = postsDAO("data/posts.json")
commentsDAO = commentsDAO("data/comments.json")

logger = logging.getLogger("basic")

@posts_blueprint.route('/')
def posts_all():
    logger.debug("Запрошены посты")
    try:
        posts = postsDAO.get_all()
        return render_template("index.html", posts = posts)
    except:
        return "Ошибка при загрузке шаблона"

@posts_blueprint.route('/posts/<int:post_pk>/')
def posts_one(post_pk):
    logger.debug(f"Запрошены посты {post_pk}")
    post_id = post_pk
    try:
        post = postsDAO.get_by_pk(post_pk)
        comments = commentsDAO.get_by_post_id(post_id)
    except (JSONDecodeError, FileNotFoundError) as err:
        return render_template("error.html", error=err)
    else:
        if post is None:
            abort(404)
        count_comments = len(comments)
        return render_template("post.html", post=post, comments=comments, count_comments=count_comments)


@posts_blueprint.route('/search/')
def posts_search():
    query = request.args.get("s", "")
    if query != "":
        posts = postsDAO.search(query)
        number_of_posts = len(posts)
    else:
        posts = []
        number_of_posts = 0

    return render_template("search.html", query=query, posts=posts, number_of_posts=number_of_posts)

@posts_blueprint.route('/users/<username>/')
def posts_by_users(username):
    posts = postsDAO.get_by_poster_name(username)
    number_of_posts = len(posts)
    return render_template("user-feed.html", posts=posts, number_of_posts=number_of_posts)

@posts_blueprint.errorhandler(404)
def error_in_load_post(err):
    return "Пост не найден", 404



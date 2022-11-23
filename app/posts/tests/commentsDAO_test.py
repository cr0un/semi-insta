import pytest

from app.posts.DAO.commentsDAO import commentsDAO

class TestCommentsDAO:

    @pytest.fixture
    def commentsDAO(self):
        return commentsDAO("tests/mock/comments.json")

    @pytest.fixture
    def our_keys(self):
        return{"pk", "comment", "commenter_name", "post_id"}

    #Получение комментариев к посту
    def test_get_by_post_pk_check_type(self, commentsDAO):
        comments = commentsDAO.get_by_post_id(1)
        assert type(comments) == list, "Результат должен быть list"
        assert type(comments[0]) == dict, "Результат должен быть dict"

    def test_get_by_post_pk_check_keys(self, commentsDAO, our_keys):
        comment = commentsDAO.get_by_post_id(1)[0]
        comments_keys = set(comment.keys())
        assert comments_keys == our_keys, "Список ключей не соответствует"


    parameters_for_posts_and_comments = [
        (1, {1,2}),
        (2, {3}),
        (3, set())
    ]

    @pytest.mark.parametrize("post_id, correct_comments_pks", parameters_for_posts_and_comments)
    def test_get_by_post_pk_check_match(self, commentsDAO, post_id, correct_comments_pks):
        comments = commentsDAO.get_by_post_id(post_id)
        comment_pks = set([comment["pk"] for comment in comments])
        assert comment_pks == correct_comments_pks, f"Не совпадает список комментариев для поста {post_id}"
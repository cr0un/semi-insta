import pytest
from app.posts.DAO.postsDAO import postsDAO

class TestPostDAO:

    @pytest.fixture
    def postsDAO(self):
        return postsDAO("data/posts.json")

    @pytest.fixture
    def our_keys(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    #Получение постов
    def test_get_all_type_check(self, postsDAO):
        posts = postsDAO.get_all()
        assert type(posts) == list, "Список постов должен быт list"
        assert type(posts[0]) == dict, "Пост должен быть dict"

    def test_get_all_check_keys(self, postsDAO, our_keys):
        posts = postsDAO.get_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())
        assert first_post_keys == our_keys, "Получены неверные ключи"

    #Получение поста
    def test_get_one_check_type(self, postsDAO):
        post = postsDAO.get_by_pk(1)
        assert type(post) == dict, "Пост должен быть dict"

    def test_get_one_check_keys(self, postsDAO, our_keys):
        post = postsDAO.get_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == our_keys, "Неверные ключи были получены"


    parameters_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize("post_pk", parameters_to_get_by_pk)
    def test_get_one_check_has_correct_pk(self, postsDAO, post_pk):
        post = postsDAO.get_by_pk(post_pk)
        post["pk"] == post_pk, "Номер полученного поста не равен запрошенному посту (его номеру)"

    #Получение по пользователю
    def test_check_type_by_poster_name_(self, postsDAO):
        posts = postsDAO.get_by_poster_name("hank")
        assert type(posts) == list, "Результат поиска по юзеру должен быть list"
        assert type(posts[0]) == dict, "Результат поиска по юзеру должен быть dict"

    def test_by_user_check_keys(self, postsDAO, our_keys):
        post = postsDAO.get_by_poster_name("hank")[0]
        post_keys = set(post.keys())
        assert post_keys == our_keys, "Получены неверные ключи"

    parameters_to_get_by_poster_name = [
        ("Jim Carry", []),
        ("johnny", [2, 6]),
        ("larry", [4, 8]),
        ("leo", [1, 5])
    ]

    @pytest.mark.parametrize("poster_name, true_posts_pk", parameters_to_get_by_poster_name)
    def test_get_by_poster_name_correct_match_posts(self, postsDAO, poster_name, true_posts_pk):
        posts = postsDAO.get_by_poster_name(poster_name)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == true_posts_pk, f"Неверный список постов по пользователю {poster_name}"


    #Поиск
    def test_search_check_type(self, postsDAO):
        posts = postsDAO.search("а")
        assert type(posts) == list, "Результат должен быть list"
        assert type(posts[0]) == dict, "Результат поиска должен быть dict"

    def test_search_check_keys(self, postsDAO, our_keys):
        post = postsDAO.search("а")[0]
        post_keys = set(post.keys())
        assert post_keys == our_keys, "Получены неверные ключи"

    queries_and_responses = [
            ("днем", [2]), ("квадратная", [1]), ("вижу", [4]), ("вот", [2,5,6], ), ("ДНЕМ", [2])
    ]

    @pytest.mark.parametrize("query, true_posts_pk", queries_and_responses)
    def test_search_correct_match(self, postsDAO, query, true_posts_pk):
        posts = postsDAO.search(query)
        pks = []
        for post in posts:
            pks.append(post["pk"])
        assert pks == true_posts_pk, f"Неверный результат поиска"



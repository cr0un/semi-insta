import json


class postsDAO:
    """ Класс отвевечает за работу со всеми поставми """
    def __init__(self, path):
        self.path = path

    def _load(self):
        with open (f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_all(self):
        """ Получаем все посты """
        return self._load()

    def get_by_pk(self, pk):
        """ Возвращает пост по его id"""
        posts = self.get_all()
        for post in posts:
            if post['pk'] == pk:
                return post

    def get_by_poster_name(self, poster_name):
        """ Возвращает пост по юзернейму"""
        posts = self.get_all()
        posts_by_poster_name = []
        for post in posts:
            if post['poster_name'] == poster_name:
                posts_by_poster_name.append(post)
        return posts_by_poster_name

    def search(self, query):
        """ Возвращаем список постов по вхождению query"""
        posts = self.get_all()
        matching_posts = []
        query_lower = query.lower()
        for post in posts:
            if query_lower in post['content'].lower():
                matching_posts.append(post)
        return matching_posts


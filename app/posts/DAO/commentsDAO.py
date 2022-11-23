import json


class commentsDAO:

    def __init__(self, path):
        self.path = path

    def comments_loader(self):
        """ Загрузка комментария """
        with open(self.path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_by_post_id(self, post_id):
        """ Загрузка комментария к посту """
        comments = self.comments_loader()
        get_by_post_id = []
        for comment in comments:
            if comment['post_id'] == post_id:
                get_by_post_id.append(comment)
        return get_by_post_id





from run import app

class TestApi:

    def test_app_all_posts_status_code(self):
        "Проверяем полученный список, верный ли он"
        response = app.test_client().get('/api/posts', follow_redirects=True)
        print(response.status_code)
        print(response.mimetype)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"

    def test_one_app_post_status_code(self):
        "Проверяем полученный список, верный ли он"
        response = app.test_client().get('/api/posts/1', follow_redirects=True)
        print(response.status_code)
        print(response.mimetype)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"
        assert response.mimetype == "application/json", "Получен не JSON"
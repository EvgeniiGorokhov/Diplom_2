from conftest import *
import allure


class TestUserUpdate:
    updated_user_data = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }

    @allure.title('Проверка ответа на запрос изменения данных аутентифицированного пользователя')
    def test_update_user_authenticated_success(self, create_new_user_and_delete):
        response = requests.patch(Urls.USER_UPDATE, headers={
            'Authorization': create_new_user_and_delete[1]['accessToken']}, data=TestUserUpdate.updated_user_data)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert deserials['user']['email'] == TestUserUpdate.updated_user_data['email']
        assert deserials['user']['name'] == TestUserUpdate.updated_user_data['name']

    @allure.title('Проверка ответа на запрос изменения данных неаутентифицированного пользователя')
    def test_update_user_unauthenticated_expected_error(self):
        response = requests.patch(Urls.USER_UPDATE, headers=Urls.HEADERS, json=TestUserUpdate.updated_user_data)
        assert response.json() == ReplyTexts.REQUEST_WITHOUT_AUTHORIZATION



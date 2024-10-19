import pytest
import allure
from urls import *
from data import *


class TestRegistration:
    @allure.title('Проверка успешной регистрации аккаунта с валидными данными')
    def test_registration_new_account_success_submit(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.USER_REGISTER, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == payload['email']
        assert deserials['user']['name'] == payload['name']
        # удаление использованных тестовых данных из базы после теста
        access_token = deserials['accessToken']
        requests.delete(Urls.USER_DELETE, headers={'Authorization': access_token})

    @allure.title('Проверка ответа на запрос регистрации с незаполненным обязательным полем')
    @pytest.mark.parametrize('credentials', UserData.CREDENTIALS_WITH_EMPTY_FIELD)
    def test_registration_one_required_field_is_empty_failed_submit(self, credentials):
        response = requests.post(Urls.USER_REGISTER, data=credentials)
        assert response.status_code == 403 and response.json() == ReplyTexts.MISSING_ONE_OF_FIELDS

    @allure.title('Проверка ответа на запрос регистрации с существующим в базе email')
    def test_registration_login_taken_failed_submit(self):
        payload = {
            'email': UserData.EMAIL,
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.USER_REGISTER, data=payload)
        assert response.status_code == 403 and response.json() == ReplyTexts.USER_EXISTS


from conftest import *
import allure


class TestAuthentication:
    @allure.title('Проверка ответа на запрос аутентификации с неверным паролем')
    def test_auth_with_wrong_passwd_expected_error(self):
        payload = {
            'email': UserData.EMAIL,
            'password': create_random_password(),
        }
        response = requests.post(Urls.USER_AUTH, data=payload)
        assert response.status_code == 401 and response.json() == ReplyTexts.AUTHORIZATION_INCORRECT_EMAIL_AND_PASSWORD

    @allure.title('Проверка ответа на запрос аутентификации с незарегистрированным email')
    def test_auth_with_wrong_login_expected_error(self):
        payload = {
            'email': create_random_email(),
            'password': UserData.PASSWORD,
        }
        response = requests.post(Urls.USER_AUTH, data=payload)
        assert response.status_code == 401 and response.json() == ReplyTexts.AUTHORIZATION_INCORRECT_EMAIL_AND_PASSWORD

    @allure.title('Проверка успешной аутентификации пользователя при передаче валидных кредов созданного аккаунта')
    def test_auth_existing_account_success(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]
        response = requests.post(Urls.USER_AUTH, data=payload)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == create_new_user_and_delete[0]['email']
        assert deserials['user']['name'] == create_new_user_and_delete[0]['name']

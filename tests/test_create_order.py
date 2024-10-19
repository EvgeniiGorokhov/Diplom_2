from conftest import *
import allure


class TestCreateOrder:
    @allure.title('Проверка ответа о создании заказа на запрос с указанными ингредиентами аутентифицированным юзером')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.BURGER, IngredientData.BURGER_1])
    def test_create_order_authenticated_user_success(self, create_new_user_and_delete, burger_ingredients):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Urls.ORDER_CREATE, data=payload, headers=headers)
        deserials = response.json()
        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'name' in deserials.keys()
        assert 'number' in deserials['order'].keys()

    @allure.title('Проверка ответа о создании заказа на запрос с указанными ингредиентами неаутентифицированным юзером')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.BURGER, IngredientData.BURGER_1])
    def test_create_order_unauthenticated_user_success(self, burger_ingredients):
        payload = {'ingredients': [burger_ingredients]}
        response = requests.post(Urls.ORDER_CREATE, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Проверка ответа при создании заказа запросом с неуказанными ингредиентами аутентифицированным юзером')
    def test_create_order_empty_ingredients_authenticated_user_expected_error(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Urls.ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 400 and response.json() == ReplyTexts.DO_NOT_TRANSFER_AN_INGREDIENT

    @allure.title('Проверка ответа при создании заказа запросом с неуказанными ингредиентами '
                  'неаутентифицированным юзером')
    def test_create_order_empty_ingredients_unauthenticated_user_expected_error(self):
        payload = {'ingredients': []}
        response = requests.post(Urls.ORDER_CREATE, data=payload, headers=Urls.HEADERS)
        assert response.status_code == 400 and response.json() == ReplyTexts.DO_NOT_TRANSFER_AN_INGREDIENT

    @allure.title('Проверка ответа при создании заказа запросом с невалидным хэшем ингредиента '
                  'аутентифицированным юзером')
    def test_create_order_invalid_ingredients_authenticated_user_expected_error(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [IngredientData.INVALID_HASH_INGREDIENT]}
        response = requests.post(Urls.ORDER_CREATE, data=payload, headers=headers)
        assert response.status_code == 500 and 'Internal Server Error' in response.text


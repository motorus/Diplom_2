from helps import Order
import pytest
import allure


class TestOrder:
    @allure.title("Создание заказа с токеном. Успешно")
    def test_create_order_with_token_success(self, new_user):
        ingredients = Order().create_burger()
        token = new_user[0].json()["accessToken"]
        response = Order.create_order(ingredients, token)
        assert response.status_code == 200
        # Проверяем что в ответе есть поле price
        # pycharm ругается на сравнение с None. Решил сделать без ошибок )
        assert response.json()["order"].get("price", "None") != "None"

    @allure.title("Создание заказа без токена. Неудача")
    def test_create_order_without_token_failed(self):
        ingredients = Order().create_burger()

        response = Order.create_order(ingredients)
        assert response.status_code == 200
        # Проверяем что в ответе есть поле price
        # pycharm ругается на сравнение с None. Решил сделать без ошибок )
        assert response.json()["order"].get("price", "None") == "None"

    @pytest.mark.parametrize("ingredients, result", [
                                                    [[], 400],
                                                    [["123123123", "456456456", "789789789"], 500]])
    @allure.title("Создание заказа с неверным списком ингредиентов. Неудача")
    def test_create_order_with_wrong_ingredients_failed(self, new_user, ingredients, result):
        token = new_user[0].json()["accessToken"]
        response = Order.create_order(ingredients, token)
        assert response.status_code == result

    @pytest.mark.parametrize("token, error_code", [
        ["with_token", 200],
        ["without_token", 401]
    ])
    @allure.title("Получение списка заказов. Успех/Неудача")
    def test_get_orders(self, new_user, token, error_code):
        user_token = new_user[0].json()["accessToken"] if token == "with_token" else ""

        response = Order.get_orders(user_token)
        assert response.status_code == error_code

import allure
from faker import Faker
import requests
from urls import EndPoints
import json
import random


class NewUserCreds:

    @staticmethod
    @allure.step("Генерация фейковых кредов для регистрации пользователя")
    def generate_creds_set(param="valid"):
        fake = Faker("ru_RU")

        email = fake.email() if param != "without_email" else ""
        password = fake.password() if param != "without_pass" else ""
        name = fake.user_name() if param != "without_name" else ""

        creds = {"email": email,
                 "password": password,
                 "name": name,
                 }
        if param == "incorrect":
            creds = {"login": "123123123",
                     "firstName": "123123123",
                     "password": "123123123"}

        return creds


class User:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def create_user(user_data):
        return requests.post(EndPoints.create_user, data=user_data)

    @staticmethod
    @allure.step("Логин существующего пользователя")
    def login_user(user_data):
        return requests.post(EndPoints.login_user, data=user_data)

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(user_token):
        headers = {"Authorization": user_token}
        response = requests.delete(EndPoints.delete_user, headers=headers)
        return response

    @staticmethod
    @allure.step("Получение данных пользователя")
    def get_user_info(user_token):
        headers = {"Authorization": user_token}
        response = requests.get(EndPoints.delete_user, headers=headers)
        return response

    @staticmethod
    @allure.step("Обновление данных пользователя")
    def update_user(user_token, new_data):
        headers = {"Authorization": user_token}
        response = requests.patch(EndPoints.update_user, headers=headers, data=new_data)
        return response


class Order:
    @staticmethod
    @allure.step("Создание нового заказа")
    def create_order(ingredients, token=""):
        headers = {"Authorization": token}
        data = {"ingredients": ingredients}
        respons = requests.post(EndPoints.create_order, data=data, headers=headers)
        return respons

    @allure.step("Создание набора хешей для нового бургера")
    def create_burger(self):
        ingredients = self.get_ingridients()
        burger_ingredients = []
        for value in ingredients.values():
            ingredient_hash = value[random.randint(0, len(value)-1)]
            burger_ingredients.append(ingredient_hash)
        return burger_ingredients

    @staticmethod
    @allure.step("Получение словаря ингредиентов с ключами по типу.")
    def get_ingridients():
        ingredients_dict = {"bun": [],
                            "main": [],
                            "sauce": []
                            }
        response = requests.get(EndPoints.ingridients)
        for ingredient in response.json()["data"]:
            current_hashs = ingredients_dict.pop(ingredient["type"])
            current_hashs.append(ingredient["_id"])
            ingredients_dict[ingredient["type"]] = current_hashs

        return ingredients_dict

    @staticmethod
    @allure.step("Получение списка закаов")
    def get_orders(token=""):
        headers = {"Authorization": token}
        response = requests.get(EndPoints.get_orders, headers=headers)
        return response

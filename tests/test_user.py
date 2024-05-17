from helps import User, NewUserCreds
import allure
import pytest


class TestUser:
    @allure.title("Проверка успешной регистрации")
    def test_registration_user_success(self, new_user):
        assert new_user[0].status_code == 200

    @allure.title("Проверка невозможности зарегистрироваться дважды с одинаковыми данными.")
    def test_double_registration_user_failed(self, new_user):
        new_user_data = new_user[1]
        registration_result = User.create_user(new_user_data)

        assert registration_result.status_code == 403
        assert registration_result.json()["success"] == False

    @pytest.mark.parametrize("user_data", [NewUserCreds.generate_creds_set("without_email"),
                                           NewUserCreds.generate_creds_set("without_pass"),
                                           NewUserCreds.generate_creds_set("without_name")])
    @allure.title("Проверка регистрации без обязательных данных. Неудача")
    def test_resistration_without_some_cred_failed(self, user_data):
        registration_result = User.create_user(user_data)
        assert registration_result.status_code == 403

    @allure.title("Проверка успешной авторизации")
    def test_login_user_success(self, new_user):

        user_data = {"email": new_user[1]["email"],
                     "password": new_user[1]["password"]}

        response = User.login_user(user_data)
        assert response.status_code == 200

    @allure.title("Проверка неудачной авторизации с корявыми данными")
    def test_login_user_failed(self):

        user_data = {"email": "123123123",
                     "password": "123123123"}

        response = User.login_user(user_data)
        assert response.status_code == 401

    @allure.title("Проверка обновления данных пользователя. Успех")
    def test_update_user_with_token_success(self, new_user):
        auth_token = new_user[0].json()["accessToken"]
        old_user_data = User.get_user_info(auth_token)
        new_user_data = NewUserCreds.generate_creds_set()
        response = User.update_user(auth_token, new_user_data)
        assert response.status_code == 200
        # проверяем что данные изменились
        assert response.json()["user"]["email"] != old_user_data.json()["user"]["email"]
        assert response.json()["user"]["name"] != old_user_data.json()["user"]["name"]
        # проверяем что пароль изменился и под ним можгно залогиниться
        login_result = User.login_user(new_user_data)
        assert login_result.status_code == 200

    @allure.title("Проверка обновления данных пользователя без предоставление токена(без авторизации). Неудача")
    def test_update_user_without_token_failed(self):
        new_user_data = {"email": "123123123",
                         "name": "123123123",
                         "password": "123123123"}

        response = User.update_user("", new_user_data)
        assert response.status_code == 401

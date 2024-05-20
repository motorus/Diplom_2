import pytest
from helps import User, NewUserCreds


@pytest.fixture(scope='function')
def new_user():
    new_user_creds = NewUserCreds.generate_creds_set()
    new_user_response = User.create_user(new_user_creds)

    yield new_user_response, new_user_creds
    User.delete_user(new_user_response.json()["accessToken"])







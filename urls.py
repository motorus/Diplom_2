
class EndPoints:
    test_url = 'https://stellarburgers.nomoreparties.site'
    ingridients     = test_url + '/api/ingredients'  # get
    create_order    = test_url + '/api/orders'  # post {"ingredients": ["123123123","456456456"]}
    password_recovery = test_url + 'api/password-reset'  # post {"email": ""}
    create_user     = test_url + '/api/auth/register'  # post {"email": "test-data@yandex.ru",
    # "password": "password",
    # "name": "Username"}
    login_user      = test_url + '/api/auth/login'  # post {"email": "", "password": ""}
    get_user_info   = test_url + '/api/auth/user'  # GET   урлы одинаковые а методы разные. Так удобнее
    update_user     = test_url + '/api/auth/user'  # PATCH
    delete_user     = test_url + '/api/auth/user'  # DELETE
    get_all_orders  = test_url + '/api/orders/all'  # GET
    get_orders      = test_url + '/api/orders'  # GET
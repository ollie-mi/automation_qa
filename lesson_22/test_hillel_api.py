from datetime import datetime
from ideas_for_test.hillel_test_api.hillel_api import *


def test_auth_signup_positive():
    """Positive test for user sign up"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json["data"]["userId"] is not None, "userId is empty"
    assert r_json["data"]["distanceUnits"] == 'km', "Key 'distanceUnits' is not 'km'"
    assert r_json["data"]["currency"] == 'usd', "Key 'currency' is not 'usd'"

    # delete user by userId
    users.users(s, r_json)


def test_auth_signup_empty_name():
    """Negative test for user sign up when name is empty"""
    request_body = {
        "name": "",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "\"name\" is not allowed to be empty"


def test_auth_signup_empty_lastname():
    """Negative test for user sign up when last name is empty"""
    request_body = {
        "name": "Harry",
        "lastName": "",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "\"lastName\" is not allowed to be empty"


def test_auth_signup_empty_email():
    """Negative test for user sign up when email is empty"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "\"email\" is not allowed to be empty"


def test_auth_signup_invalid_email():
    """Negative test for user sign up when email is invalid"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hptest.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Email is incorrect"


def test_auth_signup_empty_password():
    """Negative test for user sign up when password is empty"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "",
        "repeatPassword": "Secret12345"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "\"password\" is not allowed to be empty"


def test_auth_signup_empty_repeat_password():
    """Negative test for user sign up when repeat_password is empty"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": ""
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "\"repeatPassword\" is not allowed to be empty"


def test_auth_signup_wrong_password():
    """Negative test for user sign up when password is too short"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Sec",
        "repeatPassword": "Sec"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == ("Password has to be from 8 to 15 characters long and contain at least one integer, "
                                 "one capital, and one small letter")


def test_auth_signup_password_mismatch():
    """Negative test for user sign up when password and repeat password do not match"""
    request_body = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "123"
    }
    r = auth.signup(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Passwords do not match", "Wrong error message"


def test_car_create_positive():
    """Positive test for creating new car - user is authorized"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    request_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 201, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert r_json["data"]["id"] is not None, "id is empty"
    assert r_json["data"]["carBrandId"] == 1, "Key 'carBrandId' is not equal 1"
    assert r_json["data"]["carModelId"] == 1, "Key 'carModelId' is not equal to 1"
    assert r_json["data"]["initialMileage"] == 122, "Key 'initialMileage' is not equal to 122"

    # Get current time
    current_time = datetime.now()
    current_time = current_time.replace(second=0, microsecond=0, tzinfo=None)

    updated_mileage_at = r_json["data"]["updatedMileageAt"]
    assert updated_mileage_at is not None, "Key 'updatedMileageAt' is not empty"
    date_format = '%Y-%m-%dT%H:%M:%S.%f%z'
    updated_mileage_at_time_obj = datetime.strptime(updated_mileage_at, date_format)
    updated_mileage_at_time_obj = updated_mileage_at_time_obj.replace(second=0, microsecond=0, tzinfo=None)
    assert updated_mileage_at_time_obj == current_time, "'updatedMileageAt' time is not equal to current time"

    car_created_at = r_json["data"]["carCreatedAt"]
    assert car_created_at is not None, "Key 'carCreatedAt' is not empty"
    car_created_at_time_obj = datetime.strptime(car_created_at, date_format)
    car_created_at_time_obj = car_created_at_time_obj.replace(second=0, microsecond=0, tzinfo=None)
    assert car_created_at_time_obj == current_time, "'carCreatedAt' time is not equal to current time"

    assert r_json["data"]["mileage"] == 122, "Key 'mileage' is not equal to 122"
    assert r_json["data"]["brand"] == 'Audi', "Key 'brand' is not equal to 'Audi"
    assert r_json["data"]["model"] == 'TT', "Key 'model' is not equal to 'TT'"
    assert r_json["data"]["logo"] == 'audi.png', "Key 'logo' is not equal to 'audi.png'"

    # delete user by userId
    users.users(s, user_json)
    # delete car by id
    cars.cars_id_delete(s, r_json['data'])


def test_car_create_without_authorization():
    """Negative test for creating new car - user is not authorized"""

    request_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Not authenticated", "Wrong error message"


def test_car_create_car_brand_id_missing():
    """Negative test for creating new car - card brand id is missing"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    request_body = {
        "carModelId": 1,
        "mileage": 122
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 400, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Car brand id is required", "Wrong error message"

    # delete user by userId
    users.users(s, user_json)


def test_car_create_car_brand_not_found():
    """Negative test for creating new car - card brand is not found"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    request_body = {
        "carBrandId": 111,
        "carModelId": 1,
        "mileage": 122
    }
    r = cars.cars_post(s, request_body)
    r_json = r.json()
    assert r.status_code == 404, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Brand not found", "Wrong error message"

    # delete user by userId
    users.users(s, user_json)


def test_car_update_positive():
    """Positive test for editing existing car - user is authorized"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # create car
    request_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    car_create = cars.cars_post(s, request_body)
    car_create_json = car_create.json()
    assert car_create.status_code == 201, "Wrong status code"

    # update car
    update_data = {
        "id": car_create_json["data"]["id"],
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }
    car_update = cars.cars_id_put(s, update_data)
    car_update_json = car_update.json()

    assert car_update.status_code == 200, "Wrong status code"
    assert car_update_json["status"] == "ok", "Key 'status' is not ok"
    assert car_create_json["data"]["id"] == car_update_json["data"]["id"], "Wrong id"
    assert car_create_json["data"]["carBrandId"] == car_update_json["data"]["carBrandId"], \
        "Key 'carBrandId' has changed"
    assert car_create_json["data"]["carModelId"] == car_update_json["data"]["carModelId"], \
        "Key 'carModelId' has changed"
    assert car_create_json["data"]["initialMileage"] == car_update_json["data"]["initialMileage"], \
        "Key 'initialMileage' has changed"

    date_format = '%Y-%m-%dT%H:%M:%S.%f%z'

    car_created_at = car_update_json["data"]["carCreatedAt"]
    car_created_at_time_obj = datetime.strptime(car_created_at, date_format)

    updated_mileage_at = car_update_json["data"]["updatedMileageAt"]
    updated_mileage_at_time_obj = datetime.strptime(updated_mileage_at, date_format)

    assert car_created_at_time_obj < updated_mileage_at_time_obj, "Wrong update time"

    assert car_update_json["data"]["mileage"] == 1000, "Key 'mileage' is not equal to 1000"
    assert car_create_json["data"]["brand"] == car_update_json["data"]["brand"], "Key 'brand' has changed"
    assert car_create_json["data"]["model"] == car_update_json["data"]["model"], "Key 'model' has changed"
    assert car_create_json["data"]["logo"] == car_update_json["data"]["logo"], "Key 'logo' has changed"

    # delete user by userId
    users.users(s, user_json)
    # delete car by id
    cars.cars_id_delete(s, car_create_json['data'])


def test_car_update_without_authorization():
    """Negative test for editing existing car - user is not authorized"""

    request_body = {
        "id": 1,
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }
    r = cars.cars_id_put(s, request_body)
    r_json = r.json()
    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Not authenticated", "Wrong error message"


def test_car_update_mileage_invalid():
    """Negative test for creating new car - mileage is less than previous"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # create car
    request_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    car_create = cars.cars_post(s, request_body)
    car_create_json = car_create.json()
    assert car_create.status_code == 201, "Wrong status code"

    # update car
    update_data = {
        "id": car_create_json["data"]["id"],
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 10
    }
    car_update = cars.cars_id_put(s, update_data)
    car_update_json = car_update.json()

    assert car_update.status_code == 400, "Wrong status code"
    assert car_update_json["status"] == "error", "Key 'status' is not 'error'"
    assert car_update_json["message"] == "New mileage is less then previous entry", "Wrong error message"

    # delete user by userId
    users.users(s, user_json)
    # delete car by id
    cars.cars_id_delete(s, car_create_json['data'])


def test_car_create_car_id_not_found():
    """Negative test for creating new car - card id is not found"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # create car
    request_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 122
    }
    car_create = cars.cars_post(s, request_body)
    car_create_json = car_create.json()
    assert car_create.status_code == 201, "Wrong status code"
    car_id = car_create_json["data"]["id"]

    # delete car by id
    cars.cars_id_delete(s, car_create_json['data'])

    # update car
    update_data = {
        "id": car_id,
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }
    car_update = cars.cars_id_put(s, update_data)
    car_update_json = car_update.json()

    assert car_update.status_code == 404, "Wrong status code"
    assert car_update_json["status"] == "error", "Key 'status' is not 'error'"
    assert car_update_json["message"] == "Car not found", "Wrong error message"

    # delete user by userId
    users.users(s, user_json)


def test_car_get_users_cars_positive():
    """Positive test for getting user cars - user is authorized"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # create car 1
    car_1_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 5000
    }
    car_1 = cars.cars_post(s, car_1_body)
    car_1_json = car_1.json()
    assert car_1.status_code == 201, "Wrong status code"
    car_id_1 = car_1_json["data"]["id"]

    # create car 2
    car_2_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 1000
    }
    car_2 = cars.cars_post(s, car_2_body)
    car_2_json = car_2.json()
    assert car_2.status_code == 201, "Wrong status code"
    car_id_2 = car_2_json["data"]["id"]

    # get current user cars
    r = cars.cars_get(s)
    r_json = r.json()

    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    assert len(r_json["data"]) == 2, "Wrong amount of cars"
    assert r_json["data"][0]["id"] == car_id_1, "Wrong car_1 id"
    assert r_json["data"][1]["id"] == car_id_2, "Wrong car_2 id"

    # delete user by userId
    users.users(s, user_json)
    # delete car by id
    cars.cars_id_delete(s, car_1_json['data'])
    cars.cars_id_delete(s, car_2_json['data'])


def test_car_get_users_cars_without_authorization():
    """Negative test for getting user cars - user is not authorized"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # create car
    car_1_body = {
        "carBrandId": 1,
        "carModelId": 1,
        "mileage": 5000
    }
    car_1 = cars.cars_post(s, car_1_body)
    car_1_json = car_1.json()
    assert car_1.status_code == 201, "Wrong status code"

    # user logout
    user_logout = auth.logout(s)
    assert user_logout.status_code == 200, "Wrong status code"

    # get current user cars
    r = cars.cars_get(s)
    r_json = r.json()

    assert r.status_code == 401, "Wrong status code"
    assert r_json["status"] == "error", "Key 'status' is not 'error'"
    assert r_json["message"] == "Not authenticated", "Wrong error message"

    # user signin
    signin_data = {
        "email": "hp@test.com",
        "password": "Secret12345",
        "remember": False
    }
    user_signin = auth.signin(s, signin_data)
    assert user_signin.status_code == 200, "Wrong status code"

    # delete user by userId
    users.users(s, user_json)
    # delete car by id
    cars.cars_id_delete(s, car_1_json['data'])


def test_user_delete_positive():
    """Positive test for deleting user"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # delete user by userId
    r = users.users(s, user_json)
    r_json = r.json()
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not 'ok'"


def test_user_delete_without_authorization():
    """Negative test for deleting user - user is not authorized"""

    # create user
    user_data = {
        "name": "Harry",
        "lastName": "Potter",
        "email": "hp@test.com",
        "password": "Secret12345",
        "repeatPassword": "Secret12345"
    }
    user = auth.signup(s, user_data)
    user_json = user.json()
    assert user.status_code == 201, "Wrong status code"

    # user logout
    user_logout = auth.logout(s)
    assert user_logout.status_code == 200, "Wrong status code"

    # delete user by userId
    r = users.users(s, user_json)
    r_json = r.json()
    assert r.status_code == 401, "Wrong status code"
    assert r_json["message"] == "Not authenticated", "Wrong error message"

    # user signin
    signin_data = {
        "email": "hp@test.com",
        "password": "Secret12345",
        "remember": False
    }
    user_signin = auth.signin(s, signin_data)
    assert user_signin.status_code == 200, "Wrong status code"

    # delete user by userId
    users.users(s, user_json)

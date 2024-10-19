from helpers import *
import requests


class UserData:
    EMAIL = 'evgenii_gorokhov_13_989@gmail.com'
    PASSWORD = 'qwerty'
    USER_NAME = 'Evgenii'

    CREDENTIALS_WITH_EMPTY_FIELD = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]


class IngredientData:
    BURGER = ['61c0c5a71d1f82001bdaaa73', '61c0c5a71d1f82001bdaaa6c',
              '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    BURGER_1 = ['61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa6d',
                '61c0c5a71d1f82001bdaaa7a', '61c0c5a71d1f82001bdaaa6f']

    INVALID_HASH_INGREDIENT = ['61c0c5a71d1f8775fg657464']


class ReplyTexts:
    USER_EXISTS = {
        "success": False,
        "message": "User already exists"
    }

    MISSING_ONE_OF_FIELDS = {
        "success": False,
        "message": "Email, password and name are required fields"
    }

    AUTHORIZATION_INCORRECT_EMAIL_AND_PASSWORD = {
        "success": False,
        "message": "email or password are incorrect"
    }

    REQUEST_WITHOUT_AUTHORIZATION = {
        "success": False,
        "message": "You should be authorised"
    }
    DO_NOT_TRANSFER_AN_INGREDIENT = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }





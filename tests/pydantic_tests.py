import pytest
import requests
from pydantic import BaseModel


class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_correct():
    request = {
        "access_token": "skjsh221"
    }
    AccessTokenRequest(**request)


def test_access_token_empty():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_access_token_incorrect():
    request = {
        "access_token": 565656
    }
    AccessTokenRequest(**request)


def test_users_get_response():
    response = [
        {"id": 74567917, "first_name": "Elijah", "last_name": "Wood"},
        {"id": 72157651, "first_name": "Ian", "last_name": "McKellen"},
        {"id": 97657965, "first_name": "Sean", "last_name": "Astin"},
        {"id": 61346311, "first_name": "Viggo", "last_name": "Mortensen"},
        {"id": 23167216, "first_name": "Orlando", "last_name": "Bloom"}
    ]
    users = [User(**user) for user in response]


def test_users_get_correct_response():
    response = [
        {"id": 74567917, "first_name": "Elijah", "last_name": "Wood"},
        {"id": 72157651, "first_name": "Ian", "last_name": "McKellen"},
        {"id": 97657965, "first_name": "Sean", "last_name": "Astin"},
        {"id": 61346311, "first_name": "Viggo", "last_name": "Mortensen"},
        {"id": 23167216, "first_name": "Orlando", "last_name": "Bloom"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 5
    assert users[4].id == 23167216
    assert users[4].first_name == "Orlando"
    assert users[4].last_name == "Bloom"


def test_users_get_incorrect_response():
    response = [{"incorrect_key": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]


def test_users_get_first_user():
    response = [
        {"id": 74567917, "first_name": "Elijah", "last_name": "Wood"},
        {"id": 72157651, "first_name": "Ian", "last_name": "McKellen"},
        {"id": 97657965, "first_name": "Sean", "last_name": "Astin"},
        {"id": 61346311, "first_name": "Viggo", "last_name": "Mortensen"},
        {"id": 23167216, "first_name": "Orlando", "last_name": "Bloom"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 5
    assert users[0].id == 74567917
    assert users[0].first_name == "Elijah"
    assert users[0].last_name == "Wood"


def test_users_get_max_users():
    response = [
        {"id": i,
         "first_name": "Actor",
         "last_name": str(i)}
        for i in range(152)
]
    users = [User(**user) for user in response]
    assert len(users) == 152
    assert users[-1].id == 151
    assert users[-1].first_name == "Actor"
    assert users[-1].last_name == "151"


def test_users_get_empty():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_id_incorrect():
    user = {
        "id": "j%6^H$",
        "first_name": "Orlando",
        "last_name": "Bloom"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_first_name_int_pass():
    user = {
        "id": 23167216,
        "first_name": 23167216,
        "last_name": "Bloom"
    }
    User(**user)


def test_user_lastname_int_pass():
    user = {
        "id": 23167216,
        "first_name": "Orlando",
        "last_name": 23167216
    }
    User(**user)


def test_user_id_empty():
    user = {
        "id": "",
        "first_name": "Orlando",
        "last_name": "Bloom"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_first_name_empty_pass():
    user = {
        "id": 23167216,
        "first_name": "",
        "last_name": "Bloom"
    }
    User(**user)


def test_user_last_name_empty_pass():
    user = {
        "id": 23167216,
        "first_name": "Orlando",
        "last_name": ""
    }
    User(**user)


def test_user_info_empty():
    user = {
        "id": "",
        "first_name": "",
        "last_name": ""
    }
    with pytest.raises(ValueError):
        User(**user)
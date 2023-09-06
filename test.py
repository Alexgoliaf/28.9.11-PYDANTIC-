import pytest
import requests

from pydantic import BaseModel

class AccessTokenRequest(BaseModel):
    access_token: int

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_required():
    request = {
        "access_token": "123abs123fds"
    }
    AccessTokenRequest(**request)


def test_users_get_response():
    response = [
        {"id": 123123, "first_name": "Vika", "last_name": "Lapteva"},
        {"id": 43454323, "first_name": "Boris", "last_name": "Petrov"},
        {"id": 456665, "first_name": "Tolik", "last_name": "IOvanov"}
    ]
    users = [User(**user) for user in response]



def test_access_token_required():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_users_get_success():
    response = [
        {"id": 123123, "first_name": "Vika", "last_name": "Lapteva"},
        {"id": 43454323, "first_name": "Boris", "last_name": "Petrov"},
        {"id": 456665, "first_name": "Tolik", "last_name": "IOvanov"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 3
    assert users[0].id == 123123
    assert users[0].first_name == "Vika"
    assert users[0].last_name == "Lapteva"


def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Vika",
        "last_name": "Lapteva"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_name_format():
    user = {
        "id": 123,
        "first_name": "Vika123",
        "last_name": "Lapteva"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_lastname_format():
    user = {
        "id": 123,
        "first_name": "Vika",
        "last_name": "Lapteva123"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_users_get_one_user():
    response = [{"id": 123123, "first_name": "Vika", "last_name": "Lapteva"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 123123
    assert users[0].first_name == "Vika"
    assert users[0].last_name == "Lapteva"



def test_users_get_max_users():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1000)
]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[-1].id == 999
    assert users[-1].first_name == "User"
    assert users[-1].last_name == "999"


def test_users_get_invalid_response():
    response = [{"invalid_attr": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]
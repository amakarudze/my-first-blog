import pytest

from django.contrib.auth import get_user_model


@pytest.fixture(autouse=True)
def allow_db_access_for_all(db):
    pass


@pytest.fixture
def test_server():
    return 'https://testserver'


@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(
        username='TestUser',
        email='test@test.com',
        password='testpass1234'
    )

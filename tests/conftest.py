import pytest
from django.contrib.auth import get_user_model
from fileshare.models import file




@pytest.fixture
def user_data():
    print('user_data')
    return {'username': 'user01', 'email': 'sakibmansuri044@gmail.com', 'password1': 'user_pass543', 'password2': 'user_pass543'}


@pytest.fixture
def create_test_user(user_data):
    print('test_user')
    user_model = get_user_model()
    test_user = user_model.objects.create_user(
        username=user_data.get('username'),
        password=user_data.get('password1')
    )
    test_user.set_password(user_data.get('password1'))
    return test_user


@pytest.fixture
def created_user(client, user_data):
    user_model = get_user_model()
    test_user = user_model.objects.create_user(
        username=user_data.get('username'),
        password=user_data.get('password1')
    )
    test_user.save()
    client.login(
        username=user_data.get('username'),
        password=user_data.get('password1')
    )
    return test_user


@pytest.fixture
def file_data(create_test_user):
    return {
        'tittle': 'Test File',
        'document': r'C:\Users\sakib\OneDrive\ડેસ્કટૉપ\mysql-init.txt', 
        'user': create_test_user,
        'key': bytes([0]),
    }


@pytest.fixture
def shared_file_data(file_data, create_test_user):
    return {
        'file': file.objects.create(**file_data),
        'shared_by': create_test_user,
        'shared_with': create_test_user,
    }


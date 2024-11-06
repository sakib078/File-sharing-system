import pytest
from django import urls
from django.contrib.auth import get_user_model
from fileshare.models import file, SharedFile



@pytest.mark.parametrize('user', [
    ('register'),
    ('Login'),
    ('Logout')
])
def test_render_view(client, user):
    temp_url = urls.reverse(user)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_sigup(client, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    sigup_url = urls.reverse('register')
    resp = client.post(sigup_url, user_data)
    assert user_model.objects.count() == 1
    assert resp.status_code == 302
    assert resp.url == urls.reverse('Login')


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse('Login')
    resp = client.post(login_url, data={
        'username': user_data.get('username'),
        'password': user_data.get('password1')
    })
    assert resp.status_code == 302
    assert resp.url == urls.reverse('fileshareHome')


@pytest.mark.django_db
def test_user_logout(client, created_user):
    logout_url = urls.reverse('Logout')
    resp = client.get(logout_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_file_model(file_data):
    test_file = file.objects.create(**file_data)
    assert test_file.tittle == 'Test File'


@pytest.mark.django_db
def test_shared_file_model(shared_file_data):
    test_shared_file = SharedFile.objects.create(**shared_file_data)
    assert test_shared_file.file.tittle == 'Test File'
    assert test_shared_file.shared_by.username == 'user01'
    assert test_shared_file.shared_with.username == 'user01'

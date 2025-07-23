from http import HTTPStatus


def test_root_return_ok_and_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello, World!'}


def test_html_response(client):
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert '<h1>Hello, World!</h1>' in response.text
    assert '<p>This is a simple HTML response.</p>' in response.text
    assert '<p>Enjoy your day!</p>' in response.text


def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'email@example.com',
        'password': 'securepassword',
    }
    response = client.post('/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testuser',
        'email': 'email@example.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'testuser', 'email': 'email@example.com'}
        ]
    }


def test_update_user(client):
    data = {
        'username': 'updateduser',
        'email': 'updateuser@example.com',
        'password': 'newpassword',
    }

    response = client.put('/users/1', json=data)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'updateduser',
        'email': 'updateuser@example.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted successfully'}

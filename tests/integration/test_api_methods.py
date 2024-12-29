import time


BASE_URL = "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts(client):
    response = client.get(BASE_URL + "/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_content_type_delete(client):
    # Send a GET request
    response = client.delete(BASE_URL + "/contacts/delete/52")

    # Check if the 'Content-Type' header is present
    assert "Content-Type" in response.headers

def test_response_time_delete(client):
    start = time.time()
    response = client.delete(BASE_URL + "/contacts/delete/50")
    end = time.time()
    
    response_time = (end - start) * 1000  # Convert to milliseconds

    assert response_time < 300

def test_name_in_users(client):
    response = client.get( BASE_URL + "/contacts")
    # print(response.text)
    data = response.get_json()
    num = len(data)

    for i in range(num):
        assert "name" in data[i].keys()

def test_email_in_users(client):
    response = client.get( BASE_URL + "/contacts")
    # print(response.text)
    data = response.get_json()
    num = len(data)

    for i in range(num):
        assert "email" in data[i].keys()

def test_surname_in_users(client):
    response = client.get( BASE_URL + "/contacts")
    # print(response.text)
    data = response.get_json()
    num = len(data)

    for i in range(num):
        assert "surname" in data[i].keys()

def test_phone_in_users(client):
    response = client.get( BASE_URL + "/contacts")
    # print(response.text)
    data = response.get_json()
    num = len(data)

    for i in range(num):
        assert "phone" in data[i].keys()







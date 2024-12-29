import pytest
import requests
from forms import ContactForm

@pytest.fixture
def base_url():
    return "http://127.0.0.1:5000/"

form = ContactForm({ 
    "name":"samar",
        "surname":"hdeeb",
        "mail":"samar@mail.hdeeb",
        "phone":"1234567890"})

def test_homepage_status_code_200(base_url):
    response = requests.get(base_url)
    assert response.status_code == 200

def test_newpage_status_code_200(base_url):
    response = requests.get(base_url + "new_contact")
    assert response.status_code == 200


def test_post_method(base_url):
    payload = [
        "samar",
        "hdeeb",
        "samar@gmail.hdeeb",
        "1234567890"
    ]
    response = requests.post(base_url +" /edit_contact/48", form)
    assert response.status_code == 200

# def test_delete():
#     response = requests.delete("http://127.0.0.1:5000/contactsdelete/48") 
#     assert response.status_code == 200






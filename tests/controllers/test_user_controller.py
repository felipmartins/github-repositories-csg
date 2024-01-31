from bs4 import BeautifulSoup
from src.repositories.user_repository import UserRepository


def test_get_correct_status_code(test_client):
    response = test_client.get("/")
    assert response.status_code == 200


def test_template_title(test_client):
    response = test_client.get("/")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.title.string == "CSG International - Github Application"


def test_if_form_exists(test_client):
    response = test_client.get("/")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("form") is not None


def test_forms_action_and_method(test_client):
    response = test_client.get("/")
    soup = BeautifulSoup(response.content, "html.parser")
    assert soup.find("form")["action"] == "/"
    assert soup.find("form")["method"] == "post"


def test_if_post_insert_data_in_db(test_client, mock_config, user):
    test_client.post("/", data={"name": user.name})

    assert len(UserRepository(mock_config).find_all()) == 1

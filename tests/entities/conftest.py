import os
import pytest
from src.entities.repos import Repo
from src.entities.users import User
from src.repositories.user_repository import UserRepository


@pytest.fixture
def repos():
    return [
        Repo(
            name="repo1",
            html_url="repo1.com",
            description="repo1 description",
            language="Python",
        ),
        Repo(
            name="repo2",
            html_url="repo2.com",
            description="repo2 description",
            language="Python",
        ),
    ]


@pytest.fixture
def user(repos):
    return User(name="John", repos=repos)


@pytest.fixture
def mock_config():
    return {
        "MONGO_URI": os.getenv("MONGO_URI", "mongodb://localhost:27017"),
        "DB_NAME": os.getenv("DB_NAME", "test_csgi_test"),
    }


@pytest.fixture(autouse=True, scope="function")
def clean_db(mock_config):
    UserRepository(mock_config)._collection.drop()

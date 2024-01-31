from src.config import APP_CONFIG
from src.repositories.user_repository import UserRepository


def test_if_collection_is_correctly_defined():
    assert UserRepository(APP_CONFIG)._collection.name == "users"

from src.repositories.user_repository import UserRepository


def test_user_to_dict(user):
    result = user.to_dict()

    assert "name" in result
    assert "repos" in result

    assert len(result["repos"]) == 2


def test_if_model_initializes_correctly(user, mock_config):
    inserted_user = UserRepository(mock_config).insert(user.to_dict())
    assert inserted_user.name == user.name
    assert inserted_user.repos[0] == user.repos[0].to_dict()

    assert inserted_user.id is not None

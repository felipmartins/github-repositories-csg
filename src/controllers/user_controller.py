from fastapi import APIRouter, status, Form
from src.config import APP_CONFIG
from src.repositories.user_repository import UserRepository
from src.github_api import get_repo_data
from typing import Annotated

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def get_users():
    return [user.to_dict() for user in UserRepository(APP_CONFIG).find_all()]


@router.get("/{name}", status_code=status.HTTP_200_OK)
def get_user(name: str):
    user = UserRepository(APP_CONFIG).find_by_name(name)

    if not user:
        return {"message": "User not found"}, status.HTTP_404_NOT_FOUND

    return user


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(name: Annotated[str, Form()]):
    data = {
        "name": name,
        "repos": get_repo_data(name),
    }

    return UserRepository(APP_CONFIG).insert_or_update(name, data)

from fastapi import APIRouter, status, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from src.config import APP_CONFIG
from src.repositories.user_repository import UserRepository
from src.github_api import get_repo_data
from starlette.responses import RedirectResponse
from typing import Annotated

router = APIRouter()


templates = Jinja2Templates(directory="src/templates")


@router.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


@router.get("/{name}", status_code=status.HTTP_200_OK)
def get_user(request: Request, name: str):
    user = UserRepository(APP_CONFIG).find_by_name(name)

    if not user:
        return RedirectResponse(
            "/",
            status_code=status.HTTP_301_MOVED_PERMANENTLY,
        )

    return templates.TemplateResponse(
        "repos.html",
        {
            "request": request,
            "user": user,
        },
    )


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(name: Annotated[str, Form()]):
    data = {
        "name": name,
        "repos": get_repo_data(name),
    }

    user = UserRepository(APP_CONFIG).insert_or_update(name, data)

    return RedirectResponse(
        f"/{user.name}",
        status_code=status.HTTP_301_MOVED_PERMANENTLY,
    )

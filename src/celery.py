from celery import Celery
from src.config import APP_CONFIG
from src.github_api import get_repo_data
from src.repositories.user_repository import UserRepository


app = Celery("celery", **APP_CONFIG)

app.conf.beat_schedule = {
    "update-profiles": {
        "task": "src.celery.periodic_update",
        "schedule": 30.0,
    },
}

app.conf.timezone = "UTC"


@app.task
def update_user_data(name):
    data = {
        "name": name,
        "repos": get_repo_data(name),
        "is_new": True,
    }

    user = UserRepository(APP_CONFIG).insert_or_update(name, data)

    print(f"Updated: {user.name}")


@app.task
def periodic_update():
    for user in UserRepository(APP_CONFIG).find_all():
        update_user_data.delay(user.name)
        print(f"To update: {user.name}")

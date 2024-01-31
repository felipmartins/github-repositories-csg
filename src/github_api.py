import requests
from typing import List, Dict


def get_repo_data(name: str, amount: int = 5) -> List[Dict[str, str]]:
    response = requests.get(
        f"https://api.github.com/users/{name}/repos?per_page={amount}"
    )

    return [
        {
            "name": repo["name"],
            "description": repo["description"],
            "html_url": repo["html_url"],
            "language": repo["language"],
        }
        for repo in response.json()
    ]

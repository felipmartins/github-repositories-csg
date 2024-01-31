from dataclasses import dataclass


@dataclass
class Repo:
    name: str
    html_url: str
    description: str
    language: str

    def to_dict(self):
        return {
            "name": self.name,
            "html_url": self.html_url,
            "description": self.description,
            "language": self.language,
        }

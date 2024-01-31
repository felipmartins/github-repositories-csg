from pymongo.collection import ReturnDocument
from src.repositories.abstract_repository import BaseRepository
from src.entities.users import StoredUser
from typing import Union


class UserRepository(BaseRepository):
    @property
    def _collection(self):
        return self._db["users"]

    def _create_object(self, data: dict) -> StoredUser:
        return StoredUser(id=str(data.pop("_id")), **data)

    def find_by_name(self, name: str) -> Union[StoredUser, None]:
        data = self._collection.find_one({"name": name})
        return self._create_object(data) if data else None

    def insert(self, data: dict) -> StoredUser:
        data["is_new"] = True
        result = self._collection.insert_one(data.copy())
        return self.find_by_id(result.inserted_id)

    def update(self, name, new_data: dict) -> StoredUser:
        new_data["is_new"] = False
        update_result = self._collection.find_one_and_update(
            {"name": name},
            {"$set": new_data},
            return_document=ReturnDocument.AFTER,
        )
        return self._create_object(update_result)

    def insert_or_update(self, name: str, data: dict) -> StoredUser:
        if self.find_by_name(name):
            return self.update(name, data)
        return self.insert(data)

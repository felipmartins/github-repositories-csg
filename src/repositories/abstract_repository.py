from abc import ABC, abstractmethod
from bson import ObjectId
from pymongo import MongoClient
from pymongo.collection import Collection, ReturnDocument


class BaseRepository(ABC):
    def __init__(self, config: dict):
        client = MongoClient(config["MONGO_URI"])

        self._db = client[config["DB_NAME"]]

    @property
    @abstractmethod
    def _collection(self) -> Collection:
        """database collection that will be used"""

    @abstractmethod
    def _create_object(self, data: dict):
        """Returns the corresponding entity object"""

    def find_by_id(self, identifier):
        data = self._collection.find_one({"_id": ObjectId(identifier)})
        return self._create_object(data) if data else None

    def insert(self, data: dict):
        """Inserts a new object into the database"""
        result = self._collection.insert_one(data.copy())
        return self.find_by_id(result.inserted_id)

    def find_all(self):
        """Returns all objects from the database"""
        return [self._create_object(data) for data in self._collection.find()]

    def update(self, identifier, new_data: dict):
        update_result = self._collection.find_one_and_update(
            {"_id": ObjectId(identifier)},
            {"$set": new_data},
            return_document=ReturnDocument.AFTER,
        )
        return self._create_object(update_result)

    def delete(self, identifier):
        return self._collection.delete_one({"_id": ObjectId(identifier)})

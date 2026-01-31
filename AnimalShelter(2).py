import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv


class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self):
        """Initialize MongoDB connection using environment variables."""

        load_dotenv()

        username = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASS")
        host = os.getenv("MONGO_HOST", "nv-desktop-services.apporto.com")
        port = os.getenv("MONGO_PORT", "30685")

        if not username or not password:
            raise ValueError("Missing database credentials.")

        try:
            uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=AAC"

            self.client = MongoClient(uri)
            self.database = self.client["AAC"]
            self.collection = self.database["animals"]

        except ConnectionFailure as e:
            raise ConnectionError(f"Database connection failed: {e}")

    # ---------- CREATE ----------
    def create(self, data):

        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")

        try:
            result = self.collection.insert_one(data)
            return result.acknowledged

        except Exception as e:
            print(f"Create failed: {e}")
            return False

    # ---------- READ ----------
    def read(self, query=None):

        try:
            query = query or {}

            return list(self.collection.find(query, {"_id": False}))

        except Exception as e:
            print(f"Read failed: {e}")
            return []

    # ---------- UPDATE ----------
    def update(self, query, new_values):

        if not isinstance(new_values, dict):
            raise ValueError("Updated data must be a dictionary")

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )

            return result.modified_count

        except Exception as e:
            print(f"Update failed: {e}")
            return 0

    # ---------- DELETE ----------
    def delete(self, query):

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except Exception as e:
            print(f"Delete failed: {e}")
            return 0
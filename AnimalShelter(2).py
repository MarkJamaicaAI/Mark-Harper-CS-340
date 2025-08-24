from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB."""

    def __init__(self, username, password,
                 host='nv-desktop-services.apporto.com', port=30685):
        """Initialize MongoDB connection using pass-through parameters."""
        try:
            self.client = MongoClient(
                f"mongodb://{username}:{password}@{host}:{port}/?authSource=AAC"
            )
            self.database = self.client['AAC']
            self.collection = self.database['animals']
        except ConnectionFailure as e:
            print(f"Connection failed: {e}")
            raise

    def create(self, data):
        """Insert a document into the database."""
        if data is not None and isinstance(data, dict):
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as e:
                print(f"Create failed: {e}")
                return False
        else:
            raise Exception("Data must be a non-empty dictionary")

    def read(self, query=None):
        """
        Read documents matching the query.
        Returns JSON-safe documents (Mongo `_id` excluded).
        """
        try:
            q = query or {}
            # Exclude Mongo's _id so Dash gets JSON-serializable docs
            return list(self.collection.find(q, {"_id": False}))
        except Exception as e:
            print(f"Read failed: {e}")
            return []
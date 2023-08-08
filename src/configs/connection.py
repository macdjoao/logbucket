from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()


class DBConnectionHandler:
    def __init__(self) -> None:
        self.connection_string = os.getenv('MONGODB_URI')
        self.db_name = os.getenv('DATABASE_NAME')
        self.client = None
        self.db_connection = None

    def connect(self):
        self.client = MongoClient(self.connection_string)
        self.db_connection = self.client[self.db_name]

    def get_db_connection(self):
        return self.db_connection

    def get_client(self):
        return self.client

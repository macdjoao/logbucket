from typing import List


class LogCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.collection_name = 'logCollection'
        self.db_connection = db_connection

    def insert_one_document(self, document: dict) -> dict:
        print('chamando insert_document')
        collection = self.db_connection.get_collection(self.collection_name)
        print(collection)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, documents: List[dict]) -> List[dict]:
        collection = self.db_connection.get_collection(self.collection_name)
        collection.insert_many(documents)
        return documents

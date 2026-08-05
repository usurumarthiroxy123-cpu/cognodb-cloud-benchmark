import os
from arango import ArangoClient


class ArangoDBAdapter:

    def __init__(self):

        host = os.getenv("ARANGODB_URI")
        username = os.getenv(
            "ARANGODB_USERNAME",
            "root"
        )
        password = os.getenv(
            "ARANGODB_PASSWORD"
        )

        client = ArangoClient(
            hosts=host
        )

        self.db = client.db(
            "_system",
            username=username,
            password=password
        )


    def close(self):
        pass


    def execute_query(
            self,
            query,
            parameters=None
    ):

        cursor = self.db.aql.execute(
            query,
            bind_vars=parameters or {}
        )

        return list(cursor)


    def load_nodes(
            self,
            nodes
    ):

        collection = self.db.collection(
            "nodes"
        )

        for node in nodes:

            collection.insert(
                node
            )


    def load_relationships(
            self,
            relationships
    ):

        collection = self.db.collection(
            "relationships"
        )

        for relationship in relationships:

            collection.insert(
                relationship
            )
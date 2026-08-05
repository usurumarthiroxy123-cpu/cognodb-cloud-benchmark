from arango import ArangoClient


class ArangoDBAdapter:

    def __init__(
            self,
            uri,
            username="root",
            password=""
    ):

        client = ArangoClient(
            hosts=uri
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

        if not self.db.has_collection("nodes"):

            self.db.create_collection(
                "nodes"
            )

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

        if not self.db.has_collection("relationships"):

            self.db.create_collection(
                "relationships"
            )

        collection = self.db.collection(
            "relationships"
        )

        for relationship in relationships:

            collection.insert(
                relationship
            )
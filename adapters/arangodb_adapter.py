from arango import ArangoClient


class ArangoDBAdapter:

    def __init__(
            self,
            uri,
            username="root",
            password=""
    ):

        client = ArangoClient(
            hosts=uri,
            request_timeout=180
        )

        self.db = client.db(
            "_system",
            username=username,
            password=password
        )


    def close(self):

        pass


    def clear_database(self):

        # Delete old collections if they exist
        if self.db.has_collection("nodes"):
            self.db.delete_collection("nodes")

        if self.db.has_collection("relationships"):
            self.db.delete_collection("relationships")


        # Recreate collections
        self.db.create_collection(
            "nodes"
        )

        self.db.create_collection(
            "relationships",
            edge=True
        )


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


        batch_size = 1000


        for i in range(0, len(nodes), batch_size):

            batch = []

            for node in nodes[i:i + batch_size]:

                batch.append({

                    "_key": str(node["id"]),

                    "id": node["id"],

                    "type": node.get("type", "Node")

                })


            collection.insert_many(
                batch
            )



    def load_relationships(
            self,
            relationships
    ):

        if not self.db.has_collection("relationships"):

            self.db.create_collection(
                "relationships",
                edge=True
            )


        collection = self.db.collection(
            "relationships"
        )


        batch_size = 500


        for i in range(0, len(relationships), batch_size):

            batch = []


            for relationship in relationships[i:i + batch_size]:

                batch.append({

                    "_from": f"nodes/{relationship['source']}",

                    "_to": f"nodes/{relationship['target']}"

                })


            collection.insert_many(
                batch
            )
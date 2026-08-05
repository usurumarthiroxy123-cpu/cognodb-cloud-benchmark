import os
from neo4j import GraphDatabase


class CognoDBAdapter:

    def __init__(self):

        uri = os.getenv("COGNODB_URI")
        username = "cognodb"
        password = os.getenv("COGNODB_PASSWORD")

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password)
        )


    def close(self):

        self.driver.close()


    def execute_query(self, query, parameters=None):

        with self.driver.session() as session:

            result = session.run(
                query,
                parameters or {}
            )

            return [
                record.data()
                for record in result
            ]


    def load_nodes(self, nodes):

        query = """
        CREATE (n:Node {
            id:$id,
            type:$type
        })
        """

        with self.driver.session() as session:

            for node in nodes:

                session.run(
                    query,
                    node
                )


    def load_relationships(self, relationships):

        query = """
        MATCH (a:Node {id:$source}),
              (b:Node {id:$target})
        CREATE (a)-[:CONNECTED]->(b)
        """

        with self.driver.session() as session:

            for rel in relationships:

                session.run(
                    query,
                    rel
                )
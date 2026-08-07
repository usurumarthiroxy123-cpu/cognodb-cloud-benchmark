from neo4j import GraphDatabase


class MemgraphAdapter:

    def __init__(self, uri, username="", password=""):

        self.driver = GraphDatabase.driver(
            uri,
            auth=(username, password),
            max_connection_lifetime=300
        )


    def close(self):

        self.driver.close()


    def clear_database(self):

        with self.driver.session() as session:

            session.run(
                "MATCH (n) DETACH DELETE n"
            ).consume()

            session.run(
                "CREATE INDEX ON :Node(id)"
            ).consume()


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
        UNWIND $batch AS node

        CREATE (n:Node {
            id: node.id,
            type: node.type
        })
        """

        batch_size = 500

        with self.driver.session() as session:

            for i in range(0, len(nodes), batch_size):

                batch = nodes[i:i + batch_size]

                session.execute_write(
                    lambda tx: tx.run(
                        query,
                        batch=batch
                    ).consume()
                )


    def load_relationships(self, relationships):

        query = """
        UNWIND $batch AS rel

        MATCH (a:Node {id: rel.source}),
              (b:Node {id: rel.target})

        CREATE (a)-[:CONNECTED]->(b)
        """

        # Increased batch size to reduce cloud round trips
        batch_size = 2000

        with self.driver.session() as session:

            for i in range(0, len(relationships), batch_size):

                batch = relationships[i:i + batch_size]

                session.execute_write(
                    lambda tx: tx.run(
                        query,
                        batch=batch
                    ).consume()
                )
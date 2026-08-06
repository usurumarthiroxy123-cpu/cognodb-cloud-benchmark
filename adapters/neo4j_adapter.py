from neo4j import GraphDatabase


class Neo4jAdapter:

    def __init__(self, uri, username, password):

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


    def clear_database(self):

        query = """
        MATCH (n)
        DETACH DELETE n
        """

        with self.driver.session() as session:
            session.run(query)



    def load_nodes(self, nodes):

        query = """

        UNWIND $nodes AS node

        CREATE (n:Node)

        SET n.id = node.id,
            n.type = node.type

        """

        data = []

        if isinstance(nodes, dict):

            for node_id, node_data in nodes.items():

                data.append(
                    {
                        "id": str(node_id),
                        "type": node_data.get("type","User")
                    }
                )

        else:

            for node in nodes:

                data.append(node)


        with self.driver.session() as session:

            session.run(
                query,
                {
                    "nodes": data
                }
            ).consume()



    def load_relationships(self, relationships):

        query = """

        UNWIND $rels AS rel

        MATCH (a:Node {id: rel.source})

        MATCH (b:Node {id: rel.target})

        CREATE (a)-[:CONNECTED]->(b)

        """

        with self.driver.session() as session:

            session.run(
                query,
                {
                    "rels": relationships
                }
            ).consume()



    def get(self,node_id):

        query = """

        MATCH (n:Node {id:$id})

        RETURN n

        """

        result = self.execute_query(
            query,
            {
                "id":str(node_id)
            }
        )

        return result
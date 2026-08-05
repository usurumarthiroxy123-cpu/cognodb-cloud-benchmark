import os


def get_database_adapter(database_name):


    if database_name == "memory":

        from adapters.memory_database import MemoryDatabase

        return MemoryDatabase()



    elif database_name == "cognodb":

        from adapters.cognodb_adapter import CognoDBAdapter

        return CognoDBAdapter(
            os.getenv("COGNODB_URI"),
            os.getenv(
                "COGNODB_USERNAME",
                "cognodb"
            ),
            os.getenv("COGNODB_PASSWORD")
        )



    elif database_name == "neo4j":

        from adapters.neo4j_adapter import Neo4jAdapter

        return Neo4jAdapter(
            os.getenv("NEO4J_URI"),
            os.getenv("NEO4J_USERNAME"),
            os.getenv("NEO4J_PASSWORD")
        )



    elif database_name == "memgraph":

        from adapters.memgraph_adapter import MemgraphAdapter

        return MemgraphAdapter(
            os.getenv("MEMGRAPH_URI"),
            os.getenv(
                "MEMGRAPH_USERNAME",
                ""
            ),
            os.getenv(
                "MEMGRAPH_PASSWORD",
                ""
            )
        )



    elif database_name == "arangodb":

        from adapters.arangodb_adapter import ArangoDBAdapter

        return ArangoDBAdapter(
            os.getenv("ARANGODB_URI"),
            os.getenv(
                "ARANGODB_USERNAME",
                "root"
            ),
            os.getenv(
                "ARANGODB_PASSWORD",
                ""
            )
        )



    else:

        raise ValueError(
            f"Unsupported database: {database_name}"
        )
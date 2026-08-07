import time


def point_lookup(database, node_id):

    if database.__class__.__name__ == "ArangoDBAdapter":

        query = """
        WITH nodes

        FOR n IN nodes
        FILTER n.id == @id
        RETURN n
        """

    else:

        query = """
        MATCH (n:Node {id:$id})
        RETURN n
        """


    return database.execute_query(
        query,
        {
            "id": node_id
        }
    )



def filtered_lookup(
        database,
        property_name,
        value
):

    if database.__class__.__name__ == "ArangoDBAdapter":

        query = f"""
        WITH nodes

        FOR n IN nodes
        FILTER n.{property_name} == @value
        RETURN n.id
        """

    else:

        query = f"""
        MATCH (n:Node)
        WHERE n.{property_name} = $value
        RETURN n
        """


    return database.execute_query(
        query,
        {
            "value": value
        }
    )



def measure_lookup(
        function,
        *args,
        iterations=10
):

    latencies = []

    result = []


    for _ in range(iterations):

        start = time.perf_counter()

        result = function(*args)

        end = time.perf_counter()

        latencies.append(
            (end-start)*1000
        )


    latencies.sort()


    return {

        "matches": len(result),

        "p50_ms": round(
            latencies[int(iterations*0.5)],
            4
        ),

        "p95_ms": round(
            latencies[int(iterations*0.95)-1],
            4
        ),

        "iterations": iterations
    }
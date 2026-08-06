import time


def point_lookup(database, node_id):

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
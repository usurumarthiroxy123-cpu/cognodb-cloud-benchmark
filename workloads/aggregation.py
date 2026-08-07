import time


def count_by_property(
        database,
        property_name
):

    if database.__class__.__name__ == "ArangoDBAdapter":

        query = f"""
        WITH nodes

        FOR n IN nodes
        COLLECT value = n.{property_name} WITH COUNT INTO count
        RETURN {{
            "value": value,
            "count": count
        }}
        """

    else:
        query = """
        MATCH (n:Node)
        RETURN n.type AS value,
           count(n) AS count
        """


    return database.execute_query(
        query,
    )


def measure_aggregation(
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

        "groups": len(result),

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
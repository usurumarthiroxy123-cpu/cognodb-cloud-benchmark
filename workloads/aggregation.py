import time



def count_by_property(
        database,
        property_name
):

    query = """
    MATCH (n:Node)
    RETURN n[$property] AS property,
           count(n) AS count
    """


    return database.execute_query(
        query,
        {
            "property": property_name
        }
    )



def measure_aggregation(
        function,
        *args,
        iterations=100
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
            latencies[
                int(iterations * 0.50)
            ],
            4
        ),

        "p95_ms": round(
            latencies[
                int(iterations * 0.95)
            ],
            4
        ),

        "iterations": iterations

    }
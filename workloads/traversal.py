import time


def one_hop(database, start):

    if database.__class__.__name__ == "ArangoDBAdapter":
        query = """
WITH nodes

FOR v, e IN 1..1 OUTBOUND CONCAT("nodes/", @id)
relationships
RETURN v.id
"""

    else:

        query = """
        MATCH (a:Node {id:$id})-[:CONNECTED]->(b)
        RETURN b.id AS id
        """


    return database.execute_query(
        query,
        {
            "id": start
        }
    )



def two_hop(database, start):

    if database.__class__.__name__ == "ArangoDBAdapter":

        query = """
WITH nodes

FOR v1, e1 IN 1..1 OUTBOUND CONCAT("nodes/", @id)
relationships

FOR v2, e2 IN 1..1 OUTBOUND v1
relationships

RETURN v2.id
"""
    else:

        query = """
        MATCH (a:Node {id:$id})
              -[:CONNECTED]->()
              -[:CONNECTED]->(c)

        RETURN c.id AS id
        """


    return database.execute_query(
        query,
        {
            "id": start
        }
    )



def three_hop(database, start):

    if database.__class__.__name__ == "ArangoDBAdapter":

        query = """
WITH nodes

FOR v1, e1 IN 1..1 OUTBOUND CONCAT("nodes/", @id)
relationships

FOR v2, e2 IN 1..1 OUTBOUND v1
relationships

FOR v3, e3 IN 1..1 OUTBOUND v2
relationships

RETURN v3.id
"""

    else:

        query = """
        MATCH (a:Node {id:$id})
              -[:CONNECTED]->()
              -[:CONNECTED]->()
              -[:CONNECTED]->(d)

        RETURN d.id AS id
        """


    return database.execute_query(
        query,
        {
            "id": start
        }
    )



def measure_query(
        function,
        *args,
        iterations=100
):

    latencies = []

    result = []


    for _ in range(iterations):

        start_time = time.perf_counter()

        result = function(*args)

        end_time = time.perf_counter()


        latencies.append(
            (end_time - start_time) * 1000
        )


    latencies.sort()


    return {

        "result_count": len(result),

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
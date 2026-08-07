import random
import time
from concurrent.futures import ThreadPoolExecutor


def execute_read(database, node_id):

    if database.__class__.__name__ == "ArangoDBAdapter":
        query = """
    WITH nodes

    FOR n IN nodes
    FILTER n.id == @id
    RETURN n.id
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


def worker(database, node_id):

    start = time.perf_counter()

    execute_read(
        database,
        node_id
    )

    end = time.perf_counter()

    return (end-start)*1000



def run_mixed_workload(database):

    node_ids = [
        f"user_{i}"
        for i in range(100)
    ]


    latencies=[]


    with ThreadPoolExecutor(
        max_workers=10
    ) as executor:


        futures=[]


        for _ in range(100):

            node_id=random.choice(node_ids)

            futures.append(
                executor.submit(
                    worker,
                    database,
                    node_id
                )
            )


        for future in futures:

            latencies.append(
                future.result()
            )


    latencies.sort()


    return {

        "operations":len(latencies),

        "p50_ms":
            round(
                latencies[50],
                4
            ),

        "p95_ms":
            round(
                latencies[95],
                4
            )

    }
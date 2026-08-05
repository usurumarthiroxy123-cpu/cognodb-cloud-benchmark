import time
from concurrent.futures import ThreadPoolExecutor


def execute_read(graph, node_id):
    """
    Simulates read operation
    """

    return graph.get(node_id, [])



def execute_write(graph, node_id, value):
    """
    Simulates write operation
    """

    graph[node_id] = value

    return True



def run_mixed_workload(
        graph,
        clients=10,
        operations=100,
        read_ratio=0.7
):

    start_time = time.perf_counter()

    completed = 0


    def worker(client_id):

        nonlocal completed

        for i in range(operations):

            node_id = f"user_{i}"

            if i / operations < read_ratio:
                execute_read(graph, node_id)

            else:
                execute_write(
                    graph,
                    node_id,
                    [f"friend_{i}"]
                )

            completed += 1


    with ThreadPoolExecutor(
        max_workers=clients
    ) as executor:

        futures = []

        for client in range(clients):
            futures.append(
                executor.submit(
                    worker,
                    client
                )
            )

        for future in futures:
            future.result()


    end_time = time.perf_counter()

    total_time = end_time - start_time


    return {
        "clients": clients,
        "operations": completed,
        "queries_per_second": round(
            completed / total_time,
            2
        )
    }
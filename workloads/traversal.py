import time


def one_hop(graph, start):

    return graph.get(start, [])



def two_hop(graph, start):

    result = []

    first_level = graph.get(start, [])

    for node in first_level:

        result.extend(
            graph.get(node, [])
        )

    return result



def three_hop(graph, start):

    result = []

    first_level = graph.get(start, [])

    for node1 in first_level:

        second_level = graph.get(
            node1,
            []
        )

        for node2 in second_level:

            result.extend(
                graph.get(node2, [])
            )

    return result



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
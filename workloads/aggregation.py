import time


def count_by_property(
        nodes,
        property_name
):

    result = {}


    for node in nodes.values():

        value = node.get(
            property_name
        )


        if value not in result:

            result[value] = 0


        result[value] += 1


    return result



def measure_aggregation(
        function,
        *args,
        iterations=100
):

    latencies = []

    result = None


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
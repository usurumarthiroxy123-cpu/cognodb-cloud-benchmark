import time


def point_lookup(nodes, node_id):

    if node_id in nodes:
        return nodes[node_id]

    return None



def filtered_lookup(
        nodes,
        property_name,
        value
):

    result = []

    for node in nodes.values():

        if node.get(property_name) == value:

            result.append(node)

    return result



def measure_lookup(
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

        "matches":
            len(result)
            if isinstance(result, list)
            else 1,

        "p50_ms":
            round(
                latencies[
                    int(iterations*0.50)
                ],
                4
            ),

        "p95_ms":
            round(
                latencies[
                    int(iterations*0.95)
                ],
                4
            ),

        "iterations":
            iterations
    }
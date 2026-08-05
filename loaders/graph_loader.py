import csv


def load_nodes(path):

    nodes = {}

    with open(path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            nodes[row["id"]] = {
                "id": row["id"],
                "type": row["type"]
            }

    return nodes



def load_relationships(path):

    graph = {}

    with open(path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            source = row["source"]
            target = row["target"]


            if source not in graph:
                graph[source] = []


            graph[source].append(target)


    return graph
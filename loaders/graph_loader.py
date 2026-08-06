import csv
import time


def load_nodes(file_path):

    nodes = []

    with open(file_path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            nodes.append({
                "id": row["id"],
                "type": row["type"]
            })

    return nodes



def load_relationships(path):

    start_time = time.time()

    graph = {}

    relationship_count = 0

    with open(path, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            source = row["source"]
            target = row["target"]

            if source not in graph:
                graph[source] = []

            graph[source].append(target)

            relationship_count += 1

    end_time = time.time()

    load_time = end_time - start_time

    print(f"Relationships loaded: {relationship_count}")
    print(f"Relationship load time: {load_time:.4f} seconds")
    print(f"Relationship ingestion: {relationship_count/load_time:.2f} relationships/sec")

    return graph
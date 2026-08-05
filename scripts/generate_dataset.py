import csv
import random
import os


OUTPUT_DIR = "datasets"

NODES_FILE = os.path.join(
    OUTPUT_DIR,
    "nodes.csv"
)

RELATIONSHIPS_FILE = os.path.join(
    OUTPUT_DIR,
    "relationships.csv"
)


TOTAL_NODES = 50000
TOTAL_RELATIONSHIPS = 150000


def generate_dataset():

    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )


    print("Generating nodes...")


    with open(
        NODES_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "id",
                "type"
            ]
        )


        for i in range(
            TOTAL_NODES
        ):

            writer.writerow(
                [
                    f"user_{i}",
                    "person"
                ]
            )


    print("Generating relationships...")


    with open(
        RELATIONSHIPS_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "source",
                "target"
            ]
        )


        for _ in range(
            TOTAL_RELATIONSHIPS
        ):

            source = random.randint(
                0,
                TOTAL_NODES - 1
            )

            target = random.randint(
                0,
                TOTAL_NODES - 1
            )


            if source != target:

                writer.writerow(
                    [
                        f"user_{source}",
                        f"user_{target}"
                    ]
                )


    print(
        "Dataset generation completed"
    )

    print(
        f"Nodes: {TOTAL_NODES}"
    )

    print(
        f"Relationships: {TOTAL_RELATIONSHIPS}"
    )



if __name__ == "__main__":

    generate_dataset()
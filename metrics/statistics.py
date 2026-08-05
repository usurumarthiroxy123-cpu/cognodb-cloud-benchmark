def calculate_throughput(count, seconds):
    """
    Calculates operations per second.
    """

    if seconds == 0:
        return 0

    return round(count / seconds, 2)
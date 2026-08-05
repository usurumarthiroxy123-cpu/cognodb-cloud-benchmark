import time


def measure_loading(
        loader_function,
        *args,
        count_function=None
):

    start = time.perf_counter()

    result = loader_function(*args)

    end = time.perf_counter()


    if count_function:

        count = count_function(result)

    else:

        count = len(result)


    elapsed = end - start


    return {
        "load_time_seconds": round(
            elapsed,
            4
        ),

        "items_loaded": count,

        "items_per_second": round(
            count / elapsed,
            2
        ) if elapsed > 0 else 0
    }
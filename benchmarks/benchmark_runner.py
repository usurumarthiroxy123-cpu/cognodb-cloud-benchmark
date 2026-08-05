import time
from adapters.memory_database import MemoryDatabase


def run_benchmark(data):

    db = MemoryDatabase()

    results = {}


    start = time.time()
    db.insert(data)
    results["insert"] = round(time.time()-start,6)


    start = time.time()
    db.read()
    results["read"] = round(time.time()-start,6)


    start = time.time()
    db.query()
    results["query"] = round(time.time()-start,6)


    start = time.time()
    db.update()
    results["update"] = round(time.time()-start,6)


    return results
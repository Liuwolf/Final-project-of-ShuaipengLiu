import random
from priority_queue import MiniumPriorityQueue


def test_insert_pf(benchmark):
    def insertQueue(k):
        MiniumPriorityQueue().insert(k)
    benchmark(insertQueue, random.randint(10, 20))


def test_delMin_pf(benchmark):
    def delMinQueue(queue):
        queue.delMin()
    q = MiniumPriorityQueue()
    q.insert(random.randint(10, 20))
    benchmark(delMinQueue, q)


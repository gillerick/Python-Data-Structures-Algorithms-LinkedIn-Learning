"""
Priority queues are used in applications where resources are to be allocated based on some criteria

Methods:
    1. get (retrieves an items with the highest priority) -> dequeue
    2. put (adds item to priority queue) - > enqueue

"""
import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def put(self, item, priority):
        # Pushes element onto priority queue preserving the order of the priority
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    print(pq.is_empty())

    # Item, priority
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)
    pq.put("read the Bible", 1)
    print(pq)

    print(pq.get())
    print(pq.get())


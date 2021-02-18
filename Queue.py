"""
In a queue, all additions are made from the rear(tail) end while all removals are made from the front (head)
It is a FIFO (First In First Out)

Applications:
1. CPU - Data is transferred asynchronously between process
2. Graph traversal algorithms
3. IO buffers
4. Printer queues
5. Phone calls to customer service hotlines
6. File servers
7.Transport and operations management
8. Any other application where a resource is to be shared amongst multiple consumers


While appends and pops from the end of a list are fast, doing inserts or pops from the beginning of a list is slow
because all the other items have to be shifted by one

"""

from collections import deque


class Queue:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q)


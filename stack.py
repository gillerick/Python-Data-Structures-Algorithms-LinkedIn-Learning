class Stack:

    def __init__(self):
        self.items = []

    def __repr__(self):
        return self.items

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push("Gill")
    s.push("Erick")
    print(s)

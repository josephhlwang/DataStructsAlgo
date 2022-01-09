class Queue:
    def __init__(self):
        # Queue dynamic array implementation
        self.queue = []
        self.length = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        self.length -= 1
        return self.queue.pop(0)

    def peek(self):
        return None if self.isEmpty() else self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def __str__(self):
        return str(self.queue)


# q = Queue()
# print(q.isEmpty())
# print(q.peek())
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# print(q)
# q.dequeue()
# print(q)
# print(q.peek())
# print(q.isEmpty())

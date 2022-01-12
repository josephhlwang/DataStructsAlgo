from PriorityQueue.node import Node


class BinaryHeap:
    def __init__(self):
        # BinaryHeap is an implementation of a priority queue
        # Trees head must be the minimal value of tree; property true recursively
        # Tree struct stored in array for linear access

        self.heap = []
        self.size = 0

    def _swap(self, id1, id2):
        self.heap[id1], self.heap[id2] = self.heap[id2], self.heap[id1]

    # Node k has parent at (k-1) // 2
    def _parent(self, id):
        par = (id - 1) // 2
        return par if par >= 0 else -1

    # Node k has right and left child found at 2k+1 and 2k+2
    def _left(self, id):
        left = id * 2 + 1
        return left if left < self.size else -1

    # Node k has right and left child found at 2k+1 and 2k+2
    def _right(self, id):
        right = id * 2 + 2
        return right if right < self.size else -1

    def __str__(self):
        heap = ""
        power = 0
        count = 0
        for node in self.heap:
            heap += str(node.val) + f"({str(node.payload)}) "
            count += 1
            if count == 2 ** power:
                heap += "\n"
                power += 1
                count = 0

        return heap

    def enqueue(self, val, payload):
        # append value at next avaliable slot
        new_node = Node(val, payload)
        self.heap.append(new_node)
        self.size += 1

        # get index of new node
        cur = self.size - 1
        # get index of its parent node
        par = self._parent(cur)

        # swap cur and par while cur val < par val
        while par != -1 and self.heap[cur].val < self.heap[par].val:
            self._swap(cur, par)
            cur = par
            par = self._parent(cur)

    def peek(self):
        return self.heap[0] if not self.is_empty() else None

    def dequeue(self):
        if not self.is_empty():
            # save min val
            min_el = self.heap[0]
            # swap min val with last queued val
            self._swap(0, self.size - 1)
            # remove min
            self.heap.pop()
            self.size -= 1

            if not self.is_empty():
                # start at last queued val
                cur = 0
                left = self._left(cur)
                right = self._right(cur)
                # bubble down last queued val until position is correct
                # compare and swap with children nodes until BinaryHeap property is satisfied
                # (until its smaller than both its children)
                while left != -1:  # only check left since, if not right, then not left
                    # find min val
                    min = left
                    if right != -1 and self.heap[left].val > self.heap[right].val:
                        min = right

                    # check BH property
                    if self.heap[cur].val < self.heap[min].val:
                        return min_el
                    else:
                        self._swap(cur, min)

                        cur = min
                        left = self._left(cur)
                        right = self._right(cur)
            return min_el

        return None

    def is_empty(self):
        return self.size == 0


# h = BinaryHeap()
# h.enqueue(6, 6)
# h.enqueue(3, 3)
# h.enqueue(5, 5)
# h.enqueue(2, 2)
# h.enqueue(7, 7)
# h.enqueue(1, 1)
# h.enqueue(4, 4)
# h.enqueue(8, 8)
# print(h, "\n")
# h.dequeue()
# print(h)

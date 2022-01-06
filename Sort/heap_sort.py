# basic min heap implementation
class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _parent(self, i):
        p = (i - 1) // 2

        return None if p < 0 else p

    def _left(self, i):
        l = i * 2 + 1

        return None if l >= self.size else l

    def _right(self, i):
        r = i * 2 + 2

        return None if r >= self.size else r

    def enqueue(self, val):
        cur = self.size
        self.size += 1
        self.heap.append(val)

        par = self._parent(cur)
        while par != None:
            if self.heap[par] > self.heap[cur]:
                self._swap(par, cur)
            cur = par
            par = self._parent(cur)

    def dequeue(self):
        if self.size:
            min_val = self.heap[0]
            self._swap(0, self.size - 1)
            self.heap.pop()
            self.size -= 1
            if self.size:
                cur = 0
                left = self._left(cur)
                right = self._right(cur)
                while left != None:
                    min = left

                    if right != None and self.heap[left] > self.heap[right]:
                        min = right

                    if self.heap[cur] < self.heap[min]:
                        return min_val
                    else:
                        self._swap(min, cur)
                    cur = min
                    left = self._left(cur)
                    right = self._right(cur)

            return min_val

        return None

    def __str__(self):
        heap = ""
        power = 0
        count = 0
        for node in self.heap:
            heap += str(node) + " "
            count += 1
            if count == 2 ** power:
                heap += "\n"
                power += 1
                count = 0

        return heap


def heap_sort(arr):
    heap = MinHeap()
    # insertion cost O(nlogn)
    # n elements, each insert cost O(logn)
    for num in arr:
        heap.enqueue(num)

    # sorting cost O(nlogn)
    # n elements, each dequeue cost O(logn)
    for i in range(len(arr)):
        arr[i] = heap.dequeue()


list = [6, 4, 7, 1, 9, -2]
heap_sort(list)
print(list)

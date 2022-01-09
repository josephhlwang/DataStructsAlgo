from node import Node


class LinkedList:
    def __init__(self, head=None):
        self.length = 1 if head else 0
        self.head = head

    def is_empty(self):
        return self.length == 0

    def insert(self, val, index=None):
        if index == None:
            index = self.length

        # cannot insert outside of current length
        if index > self.length:
            print("Invalid index.")
        else:
            new_node = Node(val)

            if index == 0:
                # no head
                if self.is_empty():
                    self.head = new_node
                # replace head, join old head with new head
                else:
                    temp = self.head
                    self.head = new_node
                    self.head.next = temp
            # replace kth index, navigate to its parent, the k-1th index
            else:
                cur = self.head
                count = 0

                while count < index - 1:
                    count += 1
                    cur = cur.next

                temp = cur.next
                cur.next = new_node
                new_node.next = temp

            self.length += 1

    def __str__(self):
        li = ""
        cur = self.head

        while cur:
            li += str(cur.val) + " > "
            cur = cur.next

        return li[:-3]

    def find(self, val):
        if not self.is_empty():
            cur = self.head
            index = 0

            # linear search
            while cur:
                if val == cur.val:
                    return index
                cur = cur.next
                index += 1
        return -1

    def remove(self, index):
        if index >= self.length:
            print("Invalid index.")
        else:
            # if head, replace with next node
            if index == 0:
                self.head = self.head.next
            # navigate to the k-1 element, remove kth element
            else:
                cur = self.head
                count = 0
                while count < index - 1:
                    index -= 1
                    cur = cur.next

                # remove by replacing kth element with k+1th element
                temp = cur.next.next
                cur.next = temp

            self.length -= 1


# head = Node(6)
# ll = LinkedList()
# print(ll.is_empty())
# ll.insert(7, 0)
# ll.insert(8, 1)
# ll.insert(9, 2)
# ll.insert(8.5, 2)
# print(ll.length)
# print(ll)
# print(ll.find(8.5))
# ll.remove(1)
# print(ll.length)
# print(ll)

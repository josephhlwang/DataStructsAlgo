from node import Node


def floyds(head):

    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True

    return False


# n = Node(0)
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)

# n.next = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4

# print(floyds(n))

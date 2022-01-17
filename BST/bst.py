from node import Node


class BST:

    # BST contains a Node object as head
    # Nodes val >= Nodes left childs val; Nodes val < Nodes right childs val; Property recursively true

    def __init__(self, head=None):
        self.head = head
        self.size = 1 if head else 0

    def insert(self, val):
        new_node = Node(val)

        if self.is_empty():
            # replace head
            self.head = new_node
        else:
            # navigate to correct position
            cur = self.head
            while True:
                # go left
                if val <= cur.val:
                    if cur.left == None:
                        cur.left = new_node
                        break
                    cur = cur.left
                # go right
                else:
                    if cur.right == None:
                        cur.right = new_node
                        break
                    cur = cur.right
        self.size += 1

    def level_order(self):
        if not self.is_empty():
            # level order in trees same as BFS is graphs
            # no need to keep visited since trees have no cycles
            queue = [self.head]
            tree = ""

            # cur_level is number of nodes on current level, next_level same
            cur_level, next_level = 1, 0

            while queue:
                cur = queue.pop(0)
                tree += str(cur.val) + " "
                cur_level -= 1
                if cur.left:
                    queue.append(cur.left)
                    next_level += 1

                if cur.right:
                    queue.append(cur.right)
                    next_level += 1

                # current level of nodes done, go to next
                if cur_level == 0:
                    cur_level, next_level = next_level, 0
                    tree += "\n"

            return tree

        return ""

    def remove(self, val):
        cur = self.head

        # if node is head
        if cur and cur.val == val:
            # find replacement
            rep = self._find_replacement(cur)
            # replace children
            if rep:
                rep.left = cur.left
                rep.right = cur.right
            self.head = rep
            self.size -= 1
        # node is below head
        elif cur:
            # keep track of parent, navigate to val
            par = cur

            # cur one level down from par
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

            while cur:
                if val == cur.val:
                    # find replacement
                    rep = self._find_replacement(cur)
                    # replacement from right child

                    # check if cur is leaf
                    if rep:
                        rep.left = cur.left
                        rep.right = cur.right

                    # check which side cur is, replace cur with rep
                    if par.left and par.left.val == val:
                        par.left = rep
                    elif par.right and par.right.val == val:
                        par.right = rep

                    self.size -= 1
                    break

                # navigate to side with cur
                else:
                    if val < cur.val:
                        cur = cur.left
                    else:
                        cur = cur.right
                    if val < par.val:
                        par = par.left
                    else:
                        par = par.right

    def _find_replacement(self, node):
        # return None if node is leaf
        rep = None

        # right node exists, find replacement here
        if node.right:
            # keep track of par
            par = node.right
            # go to leftest node of par
            cur = par.left

            if cur == None:
                # par is leftest node, return it
                # unlink par from node
                node.right = par.right
                rep = par
            else:
                # navigate to leftest node
                while cur.left:
                    cur = cur.left
                    par = par.left

                # replace par left child with cur right child
                par.left = cur.right
                rep = cur

            rep.right = None
            print("here", node.right.val)

        # find replacement left
        elif node.left:
            # keep track of par
            par = node.left
            # go to rightest node of par
            cur = par.right

            if cur == None:
                # par is rightest node, return it
                # unlink par from node
                node.left = par.left
                rep = par
            else:
                # navigate to rightest node
                while cur.right:
                    cur = cur.right
                    par = par.right

                # replace par right child with cur left child
                par.right = cur.left
                rep = cur

            rep.left = None

        return rep

    def find(self, val):
        cur = self.head

        while cur:
            if cur.val == val:
                return True
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

        return False

    def is_empty(self):
        return self.size == 0


# n = Node(4)
# t = BST(n)
# t.insert(2)
# t.insert(6)
# t.insert(1)
# t.insert(3)
# t.insert(5)
# t.insert(7)

# print("size", t.size)

# print(t.level_order())
# t.remove(4)
# print(t.level_order())
# print("size", t.size)
# print(t.find(5))

n = Node(-4)
t = BST(n)
t.insert(-1)
t.insert(0)
t.insert(2)
t.remove(-1)
print(t.level_order())



class Node:
    """The singly linked list node"""
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


class CompleteBinaryTree:
    """
    Complete binary tree ADT, based on a singly linked list
    """
    t = None
    h = None
    s = 0

    def insert(self, key):
        n = Node(key)
        if self.t:
            self.t.next = n
            self.t = n
        else:
            self.t = n
            self.h = n
        self.s += 1

    def findLeftChild(self, i):
        lc_pos = 2 * i + 1
        return self.get(lc_pos)

    def findRightChild(self, i):
        rc_pos = 2 * i + 1
        return self.get(rc_pos)

    def findParent(self, p):
        if p == 0:
            return None
        pos = (p - 1) // 2
        return self.get(pos)

    def get(self, p):
        res = self.getNode(p)
        if res:
            return res.key
        return None

    def getNode(self, i):
        if self.h is None:
            return None
        node = self.h
        if i == 0:
            return node
        p = 0
        while node.next:
            node = node.next
            p += 1
            if p == i:
                return node
        return None


class MiniumPriorityQueue:
    """
    minimum priority queue
    """
    bt = CompleteBinaryTree()

    def insert(self, k):
        self.bt.insert(k)
        self.heapUp(self.bt.s - 1)

    def heapUp(self, p):
        pp = self.pPos(p)
        while pp >= 0:
            n = self.bt.getNode(p)
            pn = self.bt.getNode(pp)
            if n.key < pn.key:
                self.__swapNode(pn, n)
            p = pp
            pp = self.pPos(p)

    def delMin(self):
        if self.bt.s == 0:
            return None
        value = self.bt.get(0)
        self.__swapNode(self.bt.h, self.bt.t)
        self.__doDel()
        self.bt.s -= 1
        self.heapDown(0)
        return value

    def __doDel(self):
        if self.bt.s == 1:
            self.bt.t = None
            return
        nt = self.bt.getNode(self.bt.s - 2)
        nt.next = None
        self.bt.t = nt

    def heapDown(self, p):
        while self.lcPos(p) <= self.bt.s - 1:
            mc_pos, mc = self.__mc(p)
            node = self.bt.getNode(p)
            if node.key > mc.key:
                self.__swapNode(node, mc)
            p = mc_pos

    def __mc(self, p):
        mc_pos = self.__mcPos(p)
        return mc_pos, self.bt.getNode(mc_pos)

    def __mcPos(self, i):
        if self.rcPos(i) > self.bt.s - 1:
            return self.lcPos(i)
        else:
            if self.bt.findLeftChild(i) < self.bt.findRightChild(i):
                return self.lcPos(i)
            else:
                return self.rcPos(i)

    @staticmethod
    def __swapNode(a, b):
        tmp = b.key
        b.key = a.key
        a.key = tmp

    @staticmethod
    def pPos(pos):
        return (pos - 1) // 2

    @staticmethod
    def lcPos(pos):
        return pos * 2 + 1

    @staticmethod
    def rcPos(pos):
        return pos * 2 + 2


if __name__ == '__main__':
    queue = MiniumPriorityQueue()
    data = [4, 5, 2, 12, 3, 8, 7]
    for k in data:
        queue.insert(k)
    for i in range(len(data)):
        print(queue.delMin())



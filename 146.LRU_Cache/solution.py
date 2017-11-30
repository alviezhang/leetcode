# coding: utf-8


class Node:
    def __init__(self, *_, key=None, value=None, p=None, s=None):
        self.key = key
        self.value = value
        self.precursor = p
        self.successor = s


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self._map = dict()
        self._head = None
        self._tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self._map:
            return -1

        node = self._map[key]
        if self._head != node:
            self._pop_node(node)
            self._push_node(node)
        return self._map[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self._map:
            node = self._map[key]
            node.value = value
            self._pop_node(node)
        else:
            if self.count == self.capacity:
                self._map.pop(self._tail.key)
                self._pop_node(self._tail)

            node = Node(key=key, value=value)
            self._map[key] = node

        self._push_node(node)

    def _pop_node(self, node):
        p = node.precursor
        s = node.successor
        if node == self._tail:
            self._tail = p
        else:
            s.precursor = p

        if node == self._head:
            self._head = s
        else:
            p.successor = node.successor

        self.count -= 1
        return node

    def _push_node(self, node):
        if self.count == 0:
            self._head = node
            self._tail = node
            self.count += 1
            return

        old = self._head
        self._head = node
        old.precursor = self._head
        self._head.successor = old

        self.count += 1


if __name__ == '__main__':
    c = LRUCache(1)
    assert c.get(1) == -1
    c.put(1, 1)
    assert c.get(1) == 1
    assert c.get(1) == 1

    c = LRUCache(4)
    c.put(1, 1)
    c.put(2, 2)
    c.put(3, 3)
    c.put(4, 4)
    assert c.get(3) == 3 # 3 4 2 1
    assert c.get(1) == 1 # 1 3 4 2
    assert c.get(2) == 2 # 2 1 3 4

    c = LRUCache(1)
    c.put(2, 1)
    c.get(2)
    c.put(3, 2)
    c.get(2)
    c.get(3)

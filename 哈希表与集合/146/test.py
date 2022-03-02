class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.map:
            if self.head.next == self.map[key]:
                pass
            else:
                node = self.map[key]
                node_p = node.pre
                node_n = node.next
                node_p.next = node_n
                node_n.pre = node_p

                head_n = self.head.next
                self.head.next = node
                node.pre = self.head
                node.next = head_n
                head_n.pre = node
            return self.map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.get(key)
        elif self.capacity > 0:
            head_n = self.head.next
            node = ListNode(key, value)
            self.head.next = node
            node.pre = self.head
            node.next = head_n
            head_n.pre = node
            self.capacity -= 1
            self.map[key] = node
        else:
            tail_p = self.tail.pre
            tail_p_p = tail_p.pre
            del self.map[tail_p.key]
            tail_p_p.next = self.tail
            self.tail.pre = tail_p_p

            head_n = self.head.next
            node = ListNode(key, value)
            self.head.next = node
            node.pre = self.head
            node.next = head_n
            head_n.pre = node
            self.map[key] = node

obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

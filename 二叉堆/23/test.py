# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists):
        head = ListNode()
        tail = None
        queue = []
        count = 0
        for node in lists:
            while node:
                count += 1
                heapq.heappush(queue, (node.val, count, node))
                node = node.next
        for i in range(count):
            n = heapq.heappop(queue)[2]
            if not tail:
                head.next = n
            else:
                tail.next = n
            tail = n
        return head.next





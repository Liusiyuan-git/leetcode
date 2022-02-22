# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        newhead = lastFirstNode = firstNode = lastNode = None
        startNumber = k
        while head != None:
            t = head.next
            if startNumber == k:
                lastNode = head
            if k == 1:
                head.next = None
                firstNode, lastNode = self.reverse(lastNode)
                if newhead is None:
                    newhead = firstNode
                if lastFirstNode is not None:
                    lastFirstNode.next = firstNode
                lastFirstNode = lastNode
                k = startNumber
                head = t
                lastNode = None
                continue
            head = t
            k -= 1

        if newhead is None:
            return head
        if lastNode and lastFirstNode:
            lastFirstNode.next = lastNode
        return newhead

    def reverse(self, head):
        tail = head
        last = None
        while head != None:
            t = head.next
            head.next = last
            last = head
            head = t
        return last, tail

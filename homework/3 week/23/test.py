# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        if l > r:
            return None
        mid = (l + r) // 2
        return self.mergeTwoList(self.merge(lists, l, mid), self.merge(lists, mid + 1, r))

    def mergeTwoList(self, a, b):
        if not a:
            return b
        if not b:
            return a
        head = ListNode()
        tail = head
        aptr = a
        bptr = b
        while aptr and bptr:
            if aptr.val < bptr.val:
                tail.next = aptr
                aptr = aptr.next
            else:
                tail.next = bptr
                bptr = bptr.next
            tail = tail.next
        if aptr:
            tail.next = aptr
        if bptr:
            tail.next = bptr
        return head.next

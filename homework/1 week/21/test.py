# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        protect = ListNode()
        node = protect
        head1 = list1
        head2 = list2
        while head1 and head2:
            if head1.val <= head2.val:
                node.next = head1
                node = head1
                head1 = head1.next
            else:
                node.next = head2
                node = head2
                head2 = head2.next
            if not protect.next:
                protect.next = node

        if head1:
            node.next = head1
        if head2:
            node.next = head2
        return protect.next
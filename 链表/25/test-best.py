# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        protect = ListNode()
        last = protect
        while head is not None:
            # 1、分组（往后走k-1步，找到一组）
            # 一组的开头head 结尾end
            end = self.getEnd(head, k)
            if end is None:
                break
            next_group_head = end.next

            self.reverseList(head, next_group_head)

            last.next = end
            head.next = next_group_head
            last = head
            head = next_group_head
        return protect.next

    # 返回k-1步之后的结点
    # 返回None表示不够k个
    def getEnd(self, head, k):
        while head is not None:
            k -= 1
            if k == 0:
                return head
            head = head.next
        return None

    # 反转链表，在结点stop停止
    def reverseList(self, head, stop):
        last = head
        head = head.next
        while head != stop:
            next_head = head.next
            head.next = last
            last = head
            head = next_head

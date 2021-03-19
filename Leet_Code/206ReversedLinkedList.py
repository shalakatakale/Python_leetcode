'''206 Reversed linked list'''
# 1
class ListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None


class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        succeed = None
        while current:
            succeed = current.next
            current.next = prev
            prev = current
            current = succeed

        head = prev
        return head

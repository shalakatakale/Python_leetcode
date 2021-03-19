'''#2 Add two numbers - Linked list, Math, Recursion'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # dummy = temp = ListNode(3)
        temp = ListNode(3)  # temp is for traversal
        dummy = temp  # create dummy variable
        carry = 0
        while l1 or l2 or carry:
            # p = q = 0
            if l1:
                p = l1.val
                l1 = l1.next
            else:
                p = 0
            if l2:
                q = l2.val
                l2 = l2.next
            else:
                q = 0
            # carry, out = divmod(p+q+carry, 10)
            out = p + q + carry
            carry = out // 10
            out = out % 10
            temp.next = ListNode(out)
            temp = temp.next
        return dummy.next

# 2 RECURSION
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def printList(nodeStart):
    print(nodeStart.val)
    if nodeStart.next == None:
        return
    else:
        printList(nodeStart.next)


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        if l1 == None:
            return l2

        if l2 == None:
            return l1

        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            rval = l1.val + l2.val - 10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode
#3
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next


# 4
class Solution:
    def addTwoNumbers(self, l1, l2):
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n / 10)
            return node
        return tolist(toint(l1) + toint(l2))
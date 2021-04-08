''' #21 Merge two sorted lists
2 solutions are given below... first by making a dummy node and then making current = dummy
and adding nodes ahead of current...thus creating a new linkedlist starting with dummy...
this is the kind of thing we did in AddTwoNumbers
Second method is not creating a new node (dummy) for starting pointer but instead
assigning head to the linked list with lower first node and then using node variable to
store new linked list (just like current).
Note that we keep on reducing the l1 and l2 linked lists
  Method 3 is using recursion
 '''
class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1 is None:
            curr.next = l2
        elif l2 is None:
            curr.next = l1
        return dummy.next


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = None
        node = None
        while l1 and l2:
            if l1.val < l2.val:
                if head == None:
                    head = l1
                    node = head
                else:
                    node.next = l1
                    node = node.next
                l1= l1.next
            else:
                if head == None:
                    head = l2
                    node = head
                else:
                    node.next = l2
                    node = node.next
                l2 = l2.next
        if l1 != None:
            if head == None:
                head = l1
            else:
                node.next = l1
        else:
            if head == None:
                head = l2
            else:
                node.next = l2
        return head

# 2
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        current_1 = l1
        current_2 = l2
        while l1 or l2:
            if l1.val <= l2.val:
                temp = l1.next
                l1.next = current_2
                current_1 = temp
                current_2 = current_2.next
            else:
                temp = l2.next
                l2.next = current_1
                current_2 = l2
                current_1 = current_1.next
        if current_1:
            return current_1
        else:
            return current_2

#
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


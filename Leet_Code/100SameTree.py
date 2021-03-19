'''#100 Same Tree - Tree, Depth first search, recursion
Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node
exactly once. Space complexity : O(log(N)) in the best case of completely balanced tree and
O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.'''
"""
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q): # here p and q are two trees, we see if they are same
        if not p and not q:   # if p and q both are NULL
            return True

        if not p or not q: # if one of p and q is NULL
            return False

        if p.val != q.val:
            return False
        # recursion below
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)


## Try to understand below
from collections import deque


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

# understand below solution
class Solution:

    def isSameTree(self, p, q):
        stack = [(p, q)]
        while stack:
            (p, q) = stack.pop()
            if p and q and p.val == q.val:
                stack.extend([
                    (p.left,  q.left),
                    (p.right, q.right)
                ])
            elif p or q:
                return False
        return True








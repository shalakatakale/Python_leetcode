# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSym(L,R): # we created another function for Left and right like problem #100
            if not L and not R:
                return True
            if not L or not R:
                return False
            if L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root,root)

# read below


def isSymmetric(self, root):
    if not root:
        return True
    return self.dfs(root.left, root.right)


def dfs(self, l, r):
    if l and r:
        return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
    return l == r

# read below

def isSymmetric(self, root):
    if not root:
        return True
    stack = [(root.left, root.right)]
    while stack:
        l, r = stack.pop()
        if not l and not r:
            continue
        if not l or not r or (l.val != r.val):
            return False
        stack.append((l.left, r.right))
        stack.append((l.right, r.left))
    return True
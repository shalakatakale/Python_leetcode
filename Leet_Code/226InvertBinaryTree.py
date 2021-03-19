'''226 Invert Binary tree'''
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right =  root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


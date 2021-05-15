'''105. Leetcode Construct a binary tree from given preorder and inorder list
Not Using POP | lesser complexity in this code
for inorder list we use left and right pointer | We use dictionary for memory '''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        memory = {}
        for i, e in enumerate(inorder):
            memory[e] = i     # time - O(1)
        # here we reverse the preorder list so that the complexity for pop(last) = 1
        # because complexity for pop(0) was O(n)
        root = self.helper(preorder[::-1], inorder, 0, len(inorder), memory)

        return root

    def helper(self, preorder, inorder, leftPointer, rightPointer, memory):
        if leftPointer >= rightPointer:   # Base case because we are using recursion
            return None

        num = preorder.pop()
        root = TreeNode(num)
        idx = memory.get(num)
        print(root.val)  # this is giving you the depth first search values
        root.left = self.helper(preorder, inorder, leftPointer, idx, memory)
        root.right = self.helper(preorder, inorder, idx + 1, rightPointer, memory)
        return root

preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 7]
inorder = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]
#preorder = ['A','B','D','E','C','F']
#inorder = ['D','B','E','A','F','C']
tree = Solution()
tree.buildTree(preorder, inorder)

'''Not for leetcode but correct | Without helper class | prefer using code 2
this is not optimised but accepted | complexity is n**2  O(n**2)
105. Construct a binary tree from given preorder and inorder list'''

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        if len(preorder) == 1:
            last_node = TreeNode(preorder[0])
            return last_node

        ind = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[ind])
        # below line  is not giving you depth first search values
        print(node.value)  # this is giving you the depth first search values
        node.left = self.buildTree(preorder, inorder[:ind])
        node.right = self.buildTree(preorder, inorder[ind+1:])

        return node

preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 7]
inorder = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]

#preorder = ['A','B','D','E','C','F']
#inorder = ['D','B','E','A','F','C']
tree = Solution()
tree.buildTree(preorder, inorder)
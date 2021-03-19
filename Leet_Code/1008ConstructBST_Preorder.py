'''1008 Construct Binary Tree from Preorder list '''
class TreeNode:
    def __init__(self, value = 0):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for i in range(1,len(preorder)):
            if preorder[i] < stack[-1].value:
                node = TreeNode(preorder[i])
                stack[-1].left = node
                stack.append(node)
            else:
                while stack and preorder[i] > stack[-1].value:
                    pop = stack.pop()
                node = TreeNode(preorder[i])
                pop.right = node
                stack.append(node)
        return root
preorder = [5,3,1,4,8,6,9]
bst_preorder = Solution()
bst_preorder.bstFromPreorder(preorder)
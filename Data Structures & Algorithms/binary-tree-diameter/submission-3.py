# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxi = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)
        total = left_height + right_height + 2

        return max(total, maxi)
        
    def maxHeight(self, root):
        if not root:
            return -1
        
        return 1 + max(self.maxHeight(root.right), self.maxHeight(root.left))
        
        
        
        
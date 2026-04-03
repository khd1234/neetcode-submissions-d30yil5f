# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result1 = []
        result2 = []
        dq1 = deque([p])
        dq2 = deque([q])

        if not p:
            result1 = []
        else:
            result1.append(p.val)
            while dq1:
                node = dq1.popleft()
                # result1.append(node.val)
                
                if node.left:
                    dq1.append(node.left)
                    result1.append(node.left.val)
                else:
                    result1.append(None)
                
                if node.right:
                    dq1.append(node.right)
                    result1.append(node.right.val)
                else:
                    result1.append(None)
        if not q:
            result2 = []
        else:
            result2.append(q.val)
            while dq2:
                node = dq2.popleft()
                # result2.append(node.val)
                
                if node.left:
                    dq2.append(node.left)
                    result2.append(node.left.val)
                else:
                    result2.append(None)
                
                if node.right:
                    dq2.append(node.right)
                    result2.append(node.right.val)
                else:
                    result2.append(None)
        print(result1)
        print(result2)
        
        return result1 == result2
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, lt, rt):
        if lt is None and rt is None: return True
        if lt is None or rt is None or lt.val != rt.val: return False
        return self.helper(lt.left, rt.right) and self.helper(lt.right, rt.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.helper(root.left, root.right)
        
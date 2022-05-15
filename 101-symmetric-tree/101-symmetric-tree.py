# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def helper(lt, rt):
            if lt is None and rt is None: return True
            if lt is None or rt is None or lt.val != rt.val: return False
            return helper(lt.left, rt.right) and helper(lt.right, rt.left)

        return helper(root.left, root.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def countLevel(self, root: Optional[TreeNode], current_level: int, max_level: int) -> int:
        if root is None:
            return max_level
        
        current_level += 1
        if current_level > max_level:
            max_level = current_level
        
        max_level = self.countLevel(root.left, current_level, max_level)
        max_level = self.countLevel(root.right, current_level, max_level)
    
        return max_level
    
    def checkIsBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
    
        left_max_level = self.countLevel(root.left, 1, 1)
        right_max_level = self.countLevel(root.right, 1, 1)
        
        if abs(left_max_level - right_max_level) <= 1:
            return True
        return False
    
    def traverseEachNode(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if self.checkIsBalanced(root):
            return self.traverseEachNode(root.left) and self.traverseEachNode(root.right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.traverseEachNode(root)
    
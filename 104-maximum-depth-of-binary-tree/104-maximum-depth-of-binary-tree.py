# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseTree(self, root: Optional[TreeNode], level, max_height) -> int:
        if root.left is None and root.right is None:
            if max_height is None or level > max_height:
                max_height = level
            return max_height
        
        if root.left:
            max_height = self.traverseTree(root.left, level+1, max_height)
        
        if root.right:
            max_height = self.traverseTree(root.right, level+1, max_height)
        
        return max_height

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        return self.traverseTree(root, 1, None)
            
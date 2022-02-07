# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseTree(self, root: Optional[TreeNode], level, min_height) -> int:
        if root.left is None and root.right is None:
            if min_height is None or level < min_height:
                min_height = level
            return min_height
        if root.left:
            min_height = self.traverseTree(root.left, level+1, min_height)
        
        if root.right:
            min_height = self.traverseTree(root.right, level+1, min_height)
        return min_height

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
    
        return self.traverseTree(root, 1, None)
        
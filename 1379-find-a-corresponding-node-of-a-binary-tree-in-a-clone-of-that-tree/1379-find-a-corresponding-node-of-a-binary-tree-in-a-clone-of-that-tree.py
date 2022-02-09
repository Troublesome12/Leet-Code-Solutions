# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverseTree(self, clonedRoot: TreeNode, target: TreeNode) -> TreeNode:
        if clonedRoot is None:
            return
        
        if clonedRoot.val == target.val:
            return clonedRoot
        
        result = self.traverseTree(clonedRoot.left, target)
        if result:
            return result
        result = self.traverseTree(clonedRoot.right, target)
        return result
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        result = self.traverseTree(cloned, target)
        return result
        
        
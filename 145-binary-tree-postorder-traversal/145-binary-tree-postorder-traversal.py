# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTreeTraversal(self, root: Optional[TreeNode], result: List[int]) -> List[int]:
        if root is None:
            return
        
        self.postorderTreeTraversal(root.left, result)
        self.postorderTreeTraversal(root.right, result)
        result.append(root.val)
        
        return result 
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTreeTraversal(root, [])
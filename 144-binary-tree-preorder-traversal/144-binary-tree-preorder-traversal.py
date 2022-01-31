# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myPreorderTraversal(self, root: Optional[TreeNode], answer: List[int]) -> List[int]:
        if root is None:
            return
        
        answer.append(root.val)
        self.myPreorderTraversal(root.left, answer)
        self.myPreorderTraversal(root.right, answer)
        
        return answer
    
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.myPreorderTraversal(root, [])    
        
        
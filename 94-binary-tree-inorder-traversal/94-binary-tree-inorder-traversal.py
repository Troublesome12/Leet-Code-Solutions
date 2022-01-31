# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def myInorderTraversal(self, root: Optional[TreeNode], answer: List[int]) -> List[int]:
        if root is None:
            return
        
        self.myInorderTraversal(root.left, answer)
        answer.append(root.val)
        self.myInorderTraversal(root.right, answer)
        
        return answer
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.myInorderTraversal(root, [])

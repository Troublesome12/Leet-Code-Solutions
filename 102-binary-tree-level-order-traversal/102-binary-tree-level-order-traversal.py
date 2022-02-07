# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderTraverse(self, root: Optional[TreeNode], level, myDict: dict) -> dict:
        if root is None:
            return
        
        if level in myDict:
            myDict[level].append(root.val)
        else:
            myDict[level] = [root.val]
        
        self.levelOrderTraverse(root.left, level+1, myDict)
        self.levelOrderTraverse(root.right, level+1, myDict)
        
        return myDict
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        myDict = self.levelOrderTraverse(root, 0, {})
        myResult = []
        
        if root is None:
            return []
        
        for val in myDict.values():
            myResult.append(val)
            
        return myResult
        
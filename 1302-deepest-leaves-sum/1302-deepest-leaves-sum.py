# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverseTree(self, root, level, level_sum) -> dict:
        if root is None:
            return

        if level in level_sum:
            level_sum[level] += root.val
        else:
            level_sum[level] = root.val
        
        level += 1
        self.traverseTree(root.left, level, level_sum)
        self.traverseTree(root.right, level, level_sum)
        return level_sum
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level_sum = self.traverseTree(root, 1, {})
        return level_sum[max(level_sum.keys())]
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_duplicate = list(set(nums))

        if len(nums_duplicate) == len(nums):
            return False
        
        return True
        
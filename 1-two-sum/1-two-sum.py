class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map  = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map:
                return [i, hash_map[compliment]]
            
            else:
                hash_map[nums[i]] = i
        
        return []
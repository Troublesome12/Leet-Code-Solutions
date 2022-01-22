class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map  = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hash_map:
                a = [i+1, hash_map[compliment]+1]
                a.sort()
                return a
            
            else:
                hash_map[nums[i]] = i
        
        return []
        
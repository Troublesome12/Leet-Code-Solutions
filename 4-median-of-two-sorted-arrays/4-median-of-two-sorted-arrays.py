class Solution:
    def median(self, nums: List[int]) -> float:
        length = len(nums)
        if length % 2 == 0:
            return (nums[int((length-1)/2)] + nums[int(length/2)]) / 2
        else:
            return nums[int((length-1)/2)]
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        return self.median(nums)

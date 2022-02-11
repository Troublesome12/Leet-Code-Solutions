class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        
        isFound = False
        head = 0
        tail = len(nums)-1
        
        while(head <= tail):
            mid = (head + tail) // 2
            if nums[mid] > target:
                tail = mid-1
            
            elif nums[mid] < target:
                head = mid+1
                
            else:
                isFound = True
                break
            
        if not isFound:
            return [-1, -1]
        
        result = []
        x = mid
        while(x >= 0):
            if nums[x] == target:
                x -= 1
                if x < 0:
                    result.append(x+1)
            else:
                result.append(x+1)
                break
                
        x = mid
        while(x < len(nums)):
            if nums[x] == target:
                x += 1
                if x == len(nums):
                    result.append(x-1)
            else:
                result.append(x-1)
                break
        
        return result
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1
        currMin = 1000
        while l<= r:
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                currMin = min(currMin,nums[l])
                l = mid + 1
            else:
                currMin = min(currMin,nums[mid])
                r = mid - 1
        return currMin
            
            
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        k = 0
        nums.sort()
        while k < len(nums) - 2:
            if k > 0 and nums[k] == nums[k-1]:
                k += 1
                continue
            l , r = k+1 , len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[k] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[k] < 0:
                    l += 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            k += 1

        return res

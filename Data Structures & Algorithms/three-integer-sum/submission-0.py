class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        arr = []

        for i, num in enumerate(nums):
            if (i > 0) and (num == nums[i-1]):
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                if (num + nums[l] + nums[r]) == 0:
                    arr.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif (num + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    r -= 1

        return arr 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in found:
                return [found[complement], index]
            
            found[num] = index
        
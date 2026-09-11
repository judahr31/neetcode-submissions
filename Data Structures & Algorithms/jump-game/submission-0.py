class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        i = 0

        if i == end:
            return True

        while i <= end:
            if nums[i] + i >= end:
                return True
            
            if nums[i] == 0:
                return False

            next_best = i + 1
            max_reach = 0

            for jump in range(1, nums[i]+1):
                next_idx = i + jump

                reach = next_idx + nums[next_idx]
                if reach > max_reach:
                    max_reach = reach
                    next_best = next_idx
            
            i = next_best
        return False
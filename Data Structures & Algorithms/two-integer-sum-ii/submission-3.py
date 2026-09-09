class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers)-1

        while head < tail:
            sum = numbers[head] + numbers[tail]

            if sum == target:
                return [head+1, tail+1]
            elif sum < target:
                head += 1
            else:
                tail -= 1
            
        
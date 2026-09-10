from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest = 0

        l = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[right])
            longest = max(longest, right - l + 1)
            
        return longest
from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        possible_prefixes = set()
        longest = 0
        for n in arr1:
            while n:
                possible_prefixes.add(n)
                n //= 10
        for n in arr2:
            while n:
                if n in possible_prefixes:
                    longest = max(longest, len(str(n)))
                    break
                n //= 10
        return longest

arr1 = [1,10,100]
arr2 = [1000]
print(Solution().longestCommonPrefix(arr1, arr2))

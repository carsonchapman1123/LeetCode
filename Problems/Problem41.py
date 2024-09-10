from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        dic = {}
        for i in range(1, l + 2):
            dic[i] = False
        for n in nums:
            if n in dic:
                dic[n] = True
        for k in dic:
            if not dic[k]:
                return k
        
print(Solution().firstMissingPositive([1, 2, 3]))

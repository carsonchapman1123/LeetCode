from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return len(nums) - nums.count(val)


test = [3,2,2,3]
print(Solution().removeElement(test, 3))

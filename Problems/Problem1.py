from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for i in range(len(nums)):
            if nums[i] in comp:
                return [comp[nums[i]], i]
            else:
                comp[target - nums[i]] = i


nums = [3,3]
target = 6
print(Solution().twoSum(nums, target))

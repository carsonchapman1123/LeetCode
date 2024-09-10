from typing import List

class Solution:
    def findLeftIndex(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            current = nums[mid]
            if current < target:
                l = mid + 1
            elif current > target:
                r = mid - 1
            elif current == target:
                if mid == 0:
                    return 0
                elif nums[mid - 1] != target:
                    return mid
                else:
                    r = mid - 1
        return -1

    def findRightIndex(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            current = nums[mid]
            if current < target:
                l = mid + 1
            elif current > target:
                r = mid - 1
            elif current == target:
                if mid == len(nums) - 1:
                    return mid
                elif nums[mid + 1] != target:
                    return mid
                else:
                    l = mid + 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftIndex = self.findLeftIndex(nums, target)
        if leftIndex == -1:
            return [-1, -1]
        rightIndex = self.findRightIndex(nums, target)
        return [leftIndex, rightIndex]



testList = [1, 2, 2]
testTarg = 2
print(Solution().searchRange(testList, testTarg))

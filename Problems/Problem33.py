class Solution(object):
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if nums[length - 1] < target < nums[0]:
            return -1
        # find partition index and search
        pivot = 0
        if nums[0] > nums[length - 1]:
            l = 0
            r = length - 1
            while l <= r:
                m = (l + r) / 2
                print m
                if nums[m] == target:
                    return m
                if nums[m] > nums[m+1]:
                    pivot = m + 1
                    break
                if nums[m] < nums[0]:
                    r = m - 1
                else:
                    l = m + 1
        if pivot == 0:
            l = 0
            r = length - 1
        elif target <= nums[length - 1]:
            l = pivot
            r = length - 1
        else:
            l = 0
            r = pivot - 1
        print l, r
        while l <= r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1






testNums = [3,4,1,2]
testTarget = 2
print Solution().search(testNums, testTarget)
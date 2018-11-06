class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        i = length - 1
        while i >= 0:
            if nums[i] == val:
                del nums[i]
                length -= 1
            i -= 1
        return length


test = [3,2,2,3]
print Solution().removeElement(test, 3)
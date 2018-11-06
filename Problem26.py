class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        currentLength = n
        i = 1
        while i < currentLength:
            if nums[i] == nums[i-1]:
                del nums[i]
                currentLength -= 1
            else:
                i += 1
        print list(set(nums))
        return currentLength


test = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
print Solution().removeDuplicates(test)
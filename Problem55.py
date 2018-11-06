class Solution(object):
    def canJump(self, nums):
        steps_remaining = nums[0]
        for i in range(1, len(nums)):
            steps_remaining -= 1
            if steps_remaining == -1:
                return False
            steps_remaining = max(steps_remaining, nums[i])
        return True


test = [1,1,0,1]
print Solution().canJump(test)
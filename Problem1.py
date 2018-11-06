class Solution(object):
    def twoSum(self,nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return [dic[nums[i]], i]
            print nums[i] - target
            dic[target - nums[i]] = i


nums = [3,3]
target = 6
print Solution().twoSum(nums,target)
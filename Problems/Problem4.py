from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        avg_len = (m + n) // 2
        sorted = []
        for i in range(avg_len + 1):
            if len(nums1) == 0:
                sorted.append(nums2.pop(0))
            elif len(nums2) == 0:
                sorted.append(nums1.pop(0))
            elif nums1[0] < nums2[0]:
                sorted.append(nums1.pop(0))
            else:
                sorted.append(nums2.pop(0))
        if (m + n) % 2 == 1:
            return sorted[avg_len]
        else:
            return (sorted[avg_len] + sorted[avg_len - 1]) / 2

test1 = [1, 3]
test2 = [2, 4]
print(Solution().findMedianSortedArrays(test1,test2))

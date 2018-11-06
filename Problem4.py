class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        sorted = []
        for i in range((m+n) / 2 + 1):
            if nums1 == []:
                sorted.append(nums2[0])
                del nums2[0]
            elif nums2 == []:
                sorted.append(nums1[0])
                del nums1[0]
            elif nums1[0] < nums2[0]:
                sorted.append(nums1[0])
                del nums1[0]
            else:
                sorted.append(nums2[0])
                del nums2[0]
        if (m+n)%2 == 1:
            return sorted[(m+n) / 2]
        else:
            return (sorted[(m+n) / 2] + sorted[(m+n) / 2 - 1]) / 2.0


test1 = [1, 3]
test2 = [2, 4]
print Solution().findMedianSortedArrays(test1,test2)
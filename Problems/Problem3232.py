from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = d = 0
        for n in nums:
            if n >= 10:
                d += n
            else:
                s += n
        return s != d
    
print(Solution().canAliceWin([1, 2, 3, 4, 10]))

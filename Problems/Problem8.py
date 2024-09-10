import re

class Solution:
    def myAtoi(self, s: str) -> int:
        regex = re.search(r"^\s*[+-]?\d+", s)
        if not regex:
            return 0
        result = int(regex.group())
        maxInt = 2**31 - 1
        if result > maxInt:
            return maxInt
        minInt = -2**31
        if result < minInt:
            return minInt
        return int(regex.group())
    
print(Solution().myAtoi("  -0000000000012345678"))

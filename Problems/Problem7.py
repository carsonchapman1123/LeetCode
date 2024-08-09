class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        maxInt = (2**31 - 1) / 10
        rev = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > maxInt or (rev == maxInt and pop > 7):
                return 0
            rev = rev * 10 + pop
        if negative:
            return -1 * rev
        return rev

print(Solution().reverse(-123))

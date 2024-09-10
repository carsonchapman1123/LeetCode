class Solution(object):
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        negative = False
        if dividend < 0:
            negative = True
            dividend *= -1
        if divisor < 0:
            negative = not negative
            divisor *= -1
        if divisor == 1:
            return dividend
        while dividend >= divisor:
            dividend -= divisor
            count += 1
        if negative:
            count *= -1
        return count


print(Solution().divide(1,1))
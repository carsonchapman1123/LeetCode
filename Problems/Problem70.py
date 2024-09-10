import math
class Solution:
    def climbStairs(self, n):
        s = math.sqrt(5)
        g = (1 + s) / 2
        p = n + 1
        return int((g**p - -g**-p) / s)

    def fib(self,n):
        a = 0
        b = 1
        c = 0
        while c < n:
            temp = b
            b = a + b
            a = temp
            c += 1
        return b


print(Solution().climbStairs(4))
print(Solution().fib(6))

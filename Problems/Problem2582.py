class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = time // (n - 1)
        if r % 2 == 0:
            return time % (n - 1) + 1
        else:
            return n - (time % (n - 1))

print(Solution().passThePillow(5, 3))

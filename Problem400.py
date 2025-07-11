class Solution:
    def findNthDigit(self, n: int) -> int:
        num_digits = 1
        base = 1
        while n > 9 * base * num_digits:
            n -= 9 * base * num_digits
            num_digits += 1
            base *= 10
        digit_number = (n - 1) // num_digits
        digit_index = (n - 1) % num_digits
        final_number = base + digit_number
        return int(str(final_number)[digit_index])

s = Solution()
print(s.findNthDigit(3))
print(s.findNthDigit(11))

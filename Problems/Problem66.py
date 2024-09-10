from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        currentIndex = len(digits) - 1
        digits[currentIndex] += 1
        while digits[currentIndex] == 10 and currentIndex > 0:
            digits[currentIndex] = 0
            currentIndex -= 1
            digits[currentIndex] += 1
        if digits[0] == 10:
            digits[0] = 0
            digits = [1] + digits
        return digits

test = [9, 9, 9]
print(Solution().plusOne(test))

class Solution:
    def mySqrt(self, x: int) -> int:
        current_guess = 1.0
        while int(current_guess)**2 != x:
            next_guess = 0.5 * (current_guess + x / current_guess)
            if int(next_guess) == int(current_guess):
                return int(next_guess)
            current_guess = next_guess
        return int(current_guess)



print(Solution().mySqrt(20))

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Babylonian method. Consider using higher power of Taylor series
        '''
        current_guess = 1.0
        while int(current_guess)**2 != x:
            next_guess = 0.5 * (current_guess + x / current_guess)
            if int(next_guess) == int(current_guess):
                return int(next_guess)
            current_guess = next_guess
        return int(current_guess)
        '''
        print [1,2]+[3,4]



print Solution().mySqrt(20)
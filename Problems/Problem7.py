#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:50:58 2018

@author: macuser
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
            x *= -1
        maxInt = (2**31-1) / 10
        rev = 0
        while x != 0:
            pop = x % 10
            x /= 10
            if rev > maxInt or (rev == maxInt and pop > 7):
                return 0
            rev = rev * 10 + pop
        if negative:
            return -1 * rev
        return rev

s = Solution()
print s.reverse(-123)
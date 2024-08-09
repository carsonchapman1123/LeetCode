#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:04:40 2018

@author: macuser
"""

import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        regex = re.search(r'^\s*[+-]?\d+', str)
        if regex == None:
            return 0
        result = int(regex.group())
        maxInt = 2147483647
        if result > maxInt:
            return maxInt
        minInt = -2147483648
        if result < minInt:
            return minInt
        return int(regex.group())
    
print Solution().myAtoi("  -0000000000012345678")
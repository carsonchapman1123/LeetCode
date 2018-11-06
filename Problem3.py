#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 16:51:44 2018

@author: macuser
"""

from collections import deque

class Solution(object):
    # returns True if only contains unique chars
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substr = deque()
        length = len(s)
        longest = 0
        for i in range(length):
            currentChar = s[i]
            if currentChar not in substr:
                substr.append(currentChar)
            else:
                substrLen = len(substr)
                if substrLen > longest:
                    longest = substrLen
                while substr[0] != currentChar:
                    substr.popleft()
                substr.popleft()
                substr.append(currentChar)
        substrLen = len(substr)
        if substrLen > longest:
            longest = substrLen
        return longest
    
cl = Solution()
print cl.lengthOfLongestSubstring("abcabcaa")
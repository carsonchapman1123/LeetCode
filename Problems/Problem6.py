#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:24:34 2018

@author: macuser
"""

'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        # check if length is less than number of rows. if so return.
        if length <= numRows or numRows == 1:
            return s
        
        # otherwise initialize return string
        result = ""
        
        topCorners = length / (2*numRows-2) + 1
        print topCorners
        # append first row to return string
        i = 0
        while i < length:
            result += s[i]
            i += 2*numRows-2
        
        # append rows 1 through numRows-2
        for i in range(1,numRows-1):
            for k in range(0,topCorners):
                firstIndex = k*(2*numRows-2)+i
                secondIndex = (k+1)*(2*numRows-2)-i
                if firstIndex < length:
                    result += s[firstIndex]
                if secondIndex < length:
                    result += s[secondIndex]
        # append final row to return string
        i = numRows-1
        while i < length:
            result += s[i]
            i += 2*numRows-2
        return result
    '''
    
class Solution(object):
    def convert(self,s,numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycleLength = 2*numRows-2
        ret = ""
        for i in range(numRows):
            j = 0
            while j + i < n:
                ret += s[j + i]
                if i != 0 and i != numRows - 1 and j + cycleLength - i < n:
                    ret += s[j + cycleLength - i]
                j += cycleLength
        return ret

print Solution().convert("PAYPALISHIRING",3)
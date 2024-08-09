#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:14:18 2018

@author: macuser
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dic = {}
        for i in range(1, l + 2):
            dic[i] = False
        for n in nums:
            if n in dic:
                dic[n] = True
        for k in dic:
            if not dic[k]:
                return k
        
print Solution().firstMissingPositive([1, 2, 3])
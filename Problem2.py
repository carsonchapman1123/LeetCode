#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:36:51 2018

@author: macuser
"""

# Definition for singly-linked liste
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
def display(list):
    if list != None:
        print list.val
        display(list.next)
    else:
        print ""
    

l1 = ListNode(8)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
display(l1)

l2 = ListNode(2)
display (l2)

# could be improved by doing all in 1 traversal
'''
class Solution(object):
    def addDigits(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        l3 = ListNode(l1.val+l2.val)
        l3.next = self.addDigits(l1.next,l2.next)
        return l3
    
    def carry(self,l):
        if l == None:
            return None
        if l.val > 9:
            l.val = l.val - 10
            if l.next == None:
                l.next = ListNode(1)
            else:
                l.next.val += 1
        l.next = self.carry(l.next)
        return l
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.carry(self.addDigits(l1,l2))
'''

class Solution(object):
    def addNodes(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry == True:
                return ListNode(1)
            return None
        if l1 == None:
            l1 = ListNode(0)
        if l2 == None:
            l2 = ListNode(0)
        digit = l1.val + l2.val
        if carry == True:
            digit += 1
        carry = False
        if digit > 9:
            digit = digit - 10
            carry = True
        l3 = ListNode(digit)
        l3.next = self.addNodes(l1.next,l2.next,carry)
        return l3
    
    def addTwoNumbers(self, l1, l2):
        return self.addNodes(l1,l2,False)
        
    
l3 = Solution()
display(l3.addTwoNumbers(l1,l2))
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:11:59 2018

@author: macuser
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def display(self):
        while self != None:
            print self.val
            self = self.next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        stack = []
        count = 0
        ret = head
        while head is not None:
            count += 1
            if count == k:
                temp = head.next
                ret = head
                while stack != []:
                    head.next = stack.pop(len(stack) - 1)
                    head = head.next
                head.next = self.reverseKGroup(temp, k)
                break
            stack.append(head)
            head = head.next
        return ret
        

testHead = ListNode(1)
testHead.next = ListNode(2)
testHead.next.next = ListNode(3)
testHead.next.next.next = ListNode(4)
testHead.next.next.next.next = ListNode(5)
Solution().reverseFirstK(testHead, 3).display()
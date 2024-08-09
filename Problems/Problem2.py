# Definition for singly-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def display(self):
        if self:
            print(self.val)
            if self.next:
                self.next.display()
            else:
                print("")

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def helper(l1: ListNode | None, l2: ListNode | None, carry: bool):
            if not l1 and not l2:
                if carry is True:
                    return ListNode(1)
                return None
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            digit = l1.val + l2.val
            if carry is True:
                digit += 1
            carry = False
            if digit >= 10:
                digit = digit - 10
                carry = True
            l3 = ListNode(digit)
            l3.next = helper(l1.next,l2.next,carry)
            return l3
        return helper(l1, l2, False)
    
l1 = ListNode(8)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.display()

l2 = ListNode(2)
l2.display()

Solution().addTwoNumbers(l1,l2).display()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def toStr(self):
        ret = "["
        while self.next:
            ret += str(self.val) + ", "
            self = self.next
        return ret + str(self.val) + "]"

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        count = 1
        while curr.next and count < m:
            count += 1
            curr = curr.next
        current = curr
        front = curr.next
        curr = front
        while curr.next and count < n:
            count += 1
            temp = curr.next
            curr.next = temp.next
            temp.next = front
            front = temp
        current.next = front
        return dummy.next
    '''
    def reverseFirstK(self, head, k):
        front = head
        count = 1
        while head.next and count < k:
            count += 1
            temp = head.next
            head.next = temp.next
            temp.next = front
            front = temp
        return front

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        index = 1
        while curr.next and index < m:
            curr = curr.next
            index += 1
        curr.next = self.reverseFirstK(curr.next, n - m + 1)
        return dummy.next
    '''


head = ListNode(1)
#head.next = ListNode(2)
#'''
dummy = head
for i in range(2,6):
    head.next = ListNode(i)
    head = head.next
head = dummy
#'''
#print head.toStr()
#print Solution().reverseFirstK(head, 3).toStr()
print(Solution().reverseBetween(head, 2, 4).toStr())
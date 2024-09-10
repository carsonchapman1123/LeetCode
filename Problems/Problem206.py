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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        front = head
        while head.next:
            temp = head.next
            head.next = temp.next
            temp.next = front
            front = temp
        return front

head = ListNode(1)
dummy = head
for i in range(2,6):
    head.next = ListNode(i)
    head = head.next
head = dummy
print(Solution().reverseList(head).toStr())

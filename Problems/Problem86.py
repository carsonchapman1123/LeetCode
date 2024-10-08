# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        insertNode = None
        while head.next:
            if head.next.val >= x:
                insertNode = head
                break
            head = head.next
        while head:
            if head.val < x:
                temp = insertNode.next
                insertNode.next = head
                head.next = temp
                insertNode = insertNode.next
            head = head.next


test = ListNode(3)
test.next = ListNode(2)
test.next.next = ListNode(1)
Solution().partition(test, 2)

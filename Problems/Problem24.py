class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head.next
            head.next = self.swapPairs(temp.next)
            temp.next = head
            return temp
        return head


l = ListNode(3)
l.next = ListNode(6)
l.next.next = ListNode(9)
l.next.next = ListNode(12)

print(Solution().swapPairs1(l).next.next.val)

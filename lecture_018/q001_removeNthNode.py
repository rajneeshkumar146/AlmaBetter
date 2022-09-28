class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head

        while n > 0:
            fast = fast.next
            n -= 1

        if fast == None:
            return head.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
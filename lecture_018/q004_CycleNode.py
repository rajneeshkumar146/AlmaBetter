class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        isCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                isCycle = True
                break

        if isCycle == False:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

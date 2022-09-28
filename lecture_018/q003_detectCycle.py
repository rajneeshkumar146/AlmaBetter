class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T: O(N), S: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        isCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                isCycle = True
                break

        return isCycle

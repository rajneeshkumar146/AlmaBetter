class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T: O(2N), S: O(1)
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

    # T: O(3N), S: O(1)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tail_1 = headA
        while tail_1.next != None:
            tail_1 = tail_1.next

        tail_1.next = headB

        IntersectingNode = self.detectCycle(headA)
        tail_1.next = None

        return IntersectingNode 
        
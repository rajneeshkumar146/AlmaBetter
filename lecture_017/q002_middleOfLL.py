class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # this function we will use in every sub-problem
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev, c1 , c2 = dummy, list1, list2

        while c1 != None and c2 != None:
            if c1.val < c2.val:
                prev.next = c1
                c1 = c1.next
            else:
                prev.next = c2
                c2 = c2.next

            prev = prev.next


        if(c1 != None):
            prev.next = c1
        else: 
            prev.next = c2


        return dummy.next

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
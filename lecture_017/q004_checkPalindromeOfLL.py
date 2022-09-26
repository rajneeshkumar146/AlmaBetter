class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr != None:
            forw = curr.next  # Backup

            curr.next = prev  # link

            prev = curr # move
            curr = forw

        return prev
        
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        midNode = self.middleNode(head)
        nHead = midNode.next
        midNode.next = None
        nHead = self.reverseList(nHead)

        c1 , c2 = head, nHead
        isPalindrome = True
        while c2 != None:
            if c1.val != c2.val:
                isPalindrome = False
                break

            c1 = c1.next
            c2 = c2.next

        
        nHead = self.reverseList(nHead)
        midNode.next = nHead

        return isPalindrome

        
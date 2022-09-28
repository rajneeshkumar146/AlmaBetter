class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev, c1, c2 = dummy, list1, list2

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

    def mergeKLists_01(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ansList = None
        for list in lists:
            ansList = self.mergeTwoLists(ansList, list)

        return ansList

    def mergeKLists_helper(self, lists: List[Optional[ListNode]], si, ei) -> Optional[ListNode]:
        if(si == ei):
            return lists[si]

        mid = (si + ei) // 2
        leftList = self.mergeKLists_helper(lists, si, mid)
        rightList = self.mergeKLists_helper(lists, mid + 1, ei)

        return self.mergeTwoLists(leftList, rightList)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return None
        return self.mergeKLists_helper(lists, 0, l - 1)

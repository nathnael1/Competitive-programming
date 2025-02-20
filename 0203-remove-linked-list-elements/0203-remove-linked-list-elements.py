# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #edge case
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        if not head:
            return None
        while curr:
            if curr.next:
                if curr.next.val == val:
                    curr.next =curr.next.next
                    continue
                else:
                    curr = curr.next
            else:
                curr = curr.next
        return dummy.next
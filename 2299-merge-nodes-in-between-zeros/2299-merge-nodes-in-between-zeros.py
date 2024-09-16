# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        value = 0
        while head:
            if head.val == 0 and value!=0:
                dummy.next = ListNode(value)
                dummy =dummy.next
                value = 0
            else:
                value += head.val
            head = head.next
        return res.next
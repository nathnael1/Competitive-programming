# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = []
        while head is not None:
            res.append(head.val)
            head = head.next
        res.sort()
        head = ListNode(res[0])
        temp = head
        for i in res[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head
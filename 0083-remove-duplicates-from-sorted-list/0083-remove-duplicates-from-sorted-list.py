# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #checking the current and the future head
        res = head
        while head:
            if head and head.next:
                if head.val == head.next.val:
                    head.next = head.next.next
                else:
                    head = head.next
            else:
                head = head.next
        return res
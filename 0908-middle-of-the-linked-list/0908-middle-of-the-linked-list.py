# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #using 2 pointer technique
        right = head
        while right and right.next:
            right= right.next.next
            head = head.next
        return head
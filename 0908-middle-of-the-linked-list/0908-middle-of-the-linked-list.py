# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #finding the total length
        dummy = head
        length = 0
        while dummy:
            length+=1
            dummy = dummy.next
        middle = length//2
        while head:
            if middle == 0:
                break
            head = head.next
            middle-=1
        return head

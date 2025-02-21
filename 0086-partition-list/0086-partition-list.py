# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        #left and right dummy
        left = ListNode()
        right = ListNode()
        dummy_left = left
        dummy_right = right
        while head:
            if head.val < x:
                temp = head
                head = head.next
                temp.next = None
                dummy_left.next = temp
                dummy_left = dummy_left.next
                
                
            elif head.val >= x:
                temp = head
                head = head.next
                temp.next = None
                dummy_right.next = temp
                dummy_right = dummy_right.next
                

        dummy_left.next = right.next
        return left.next
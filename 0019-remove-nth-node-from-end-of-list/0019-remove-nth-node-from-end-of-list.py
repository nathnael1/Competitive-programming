# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reversing the linked list
        reversed_linked = None
        while head:
            next_node = head.next
            head.next = reversed_linked
            reversed_linked = head
            head = next_node
        #creating a dummy
        dummy = ListNode()
        dummy.next = reversed_linked
        res = dummy
        index = 1
        while dummy:
            if index == n and dummy.next:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            index+=1
        prev = None
        res = res.next
        while res:
            next_node = res.next
            res.next  =prev
            prev = res
            res = next_node
        return prev



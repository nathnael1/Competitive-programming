# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_res = ListNode()
        curr = sorted_res
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                temp.next = None
                curr.next = temp
                curr = curr.next
            else:
                temp = list2
                list2 = list2.next
                temp.next = None
                curr.next = temp
                curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
            
        return sorted_res.next


                
        
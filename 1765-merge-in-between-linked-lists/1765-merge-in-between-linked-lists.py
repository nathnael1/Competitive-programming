# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        curr2 = list2
        index = 0
        while curr1:
            if index == a-1:
                nodeBeforeA= curr1
            if index == b+1:
                nodeAfterB= curr1
            curr1 = curr1.next
            index+=1
        if nodeBeforeA:
            nodeBeforeA.next = curr2
        while curr2.next:
            curr2 =curr2.next
        if nodeAfterB:
            curr2.next = nodeAfterB
        return list1
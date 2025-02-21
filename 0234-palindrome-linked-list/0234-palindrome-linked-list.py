# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        dummy = head
        while dummy:
            temp = ListNode(dummy.val)
            temp.next = prev
            prev = temp
            dummy = dummy.next
        #checking if it is palindrome
        while head and temp:
            if head.val != temp.val:
                return False
            head = head.next
            temp = temp.next
        return True

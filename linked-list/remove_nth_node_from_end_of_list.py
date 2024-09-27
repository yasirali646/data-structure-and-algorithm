"""
    Remove Nth Node From End of List
    
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return dummy.next
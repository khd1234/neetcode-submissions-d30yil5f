# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        index = length - n 
        if index == 0:
            return head.next

        node = head
        i = 0
        while i < index - 1:
            node = node.next
            i += 1
        temp = node.next.next
        node.next = temp

        return head
        

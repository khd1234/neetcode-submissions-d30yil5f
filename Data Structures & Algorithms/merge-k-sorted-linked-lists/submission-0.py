# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = result = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next

            result = result.next
        
        result.next = list1 or list2
        
        return head.next   

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            newLis = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None
                
                newLis.append(self.mergeTwoLists(first, second))
                
            print(newLis)
            lists = newLis
        
        if lists:
            return lists[0]
        
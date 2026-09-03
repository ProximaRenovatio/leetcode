from utils.linked_list import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        if not list1:
            return list2
        elif not list2: 
            return list1

        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp
        
        head = list1
        
        while list2:
            if not list1.next:
                list1.next = list2
                return head
            elif list1.next.val > list2.val:
                temp1 = list1.next
                temp2 = list2.next
                list1.next = list2
                list2.next = temp1
                list2 = temp2
                
            else:
                list1 = list1.next
                
        return head
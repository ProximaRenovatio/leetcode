from utils.linked_list import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        res = [-1,-1]
        i = 1
        first_Cr = 0
        last_Cr = 0

        # loop on all the nodes
        while head.next:
            current = head.next

            # the current node could be critical only if there is another node after it   
            if current.next:

                # condition to identify minima and maxima points
                if (current.val < head.val and current.val < current.next.val or 
                current.val > head.val and current.val > current.next.val):

                    # if already a critical point exists other than the current, update the minimum distance
                    if first_Cr:
                        if res[0] > -1:
                            res[0] = min(res[0], i - last_Cr)
                        else:
                            res[0] = i - last_Cr

                    # track the position of the last critical point
                    last_Cr = i

                    # if the current is the first ones, track the position
                    if not first_Cr:
                        first_Cr = i            

            i += 1
            head = current

            # calculate the maximum distance if there are at least 2 critical points
            res[1] = last_Cr - first_Cr if last_Cr != first_Cr else -1

        return res
        
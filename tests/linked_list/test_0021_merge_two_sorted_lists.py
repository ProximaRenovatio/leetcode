from solutions.linked_list.easy._0021_merge_two_sorted_lists import Solution
from utils.linked_list import ListNode

def test_merge_two_sorted_lists():
    solution = Solution()

    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    result = solution.mergeTwoLists(list1, list2)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    assert values == [1, 1, 2, 3, 4, 4]

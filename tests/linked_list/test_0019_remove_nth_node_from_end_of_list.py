from solutions.linked_list.medium._0019_remove_nth_node_from_end_of_list import Solution

def test_remove_nth_node_from_end_of_list():
    solution = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.removeNthFromEnd(head, 2)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    assert values == [1, 2, 3, 5]

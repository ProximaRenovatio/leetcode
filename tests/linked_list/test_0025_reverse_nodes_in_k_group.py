from solutions.linked_list.hard._0025_reverse_nodes_in_k_group import Solution

def test_reverse_nodes_in_k_group():
    solution = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseKGroup(head, 2)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    assert values == [2, 1, 4, 3, 5]

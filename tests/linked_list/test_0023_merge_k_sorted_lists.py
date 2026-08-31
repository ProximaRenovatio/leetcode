from solutions.linked_list.hard._0023_merge_k_sorted_lists import Solution

def test_merge_k_sorted_lists():
    solution = Solution()

    lists = [
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]

    result = solution.mergeKLists(lists)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    assert values == [1, 1, 2, 3, 4, 4, 5, 6]

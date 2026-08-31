from solutions.linked_list.easy._0206_reverse_linked_list import Solution

def test_reverse_linked_list():
    solution = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    result = solution.reverseList(head)

    values = []
    while result:
        values.append(result.val)
        result = result.next

    assert values == [5, 4, 3, 2, 1]

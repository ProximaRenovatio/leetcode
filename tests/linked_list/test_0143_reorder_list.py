from solutions.linked_list.medium._0143_reorder_list import Solution

def test_reorder_list():
    solution = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    solution.reorderList(head)

    values = []
    node = head

    while node:
        values.append(node.val)
        node = node.next

    assert values == [1, 4, 2, 3]

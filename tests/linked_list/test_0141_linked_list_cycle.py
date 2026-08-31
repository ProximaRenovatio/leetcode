from solutions.linked_list.easy._0141_linked_list_cycle import Solution

def test_linked_list_cycle():
    solution = Solution()

    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    assert solution.hasCycle(head) is True

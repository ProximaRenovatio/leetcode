from solutions.linked_list.medium._0138_copy_list_with_random_pointer import Solution

def test_copy_list_with_random_pointer():
    solution = Solution()

    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    result = solution.copyRandomList(node1)

    assert result is not node1
    assert result.val == 7
    assert result.next.val == 13

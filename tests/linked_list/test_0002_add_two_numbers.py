from solutions.linked_list.medium._0002_add_two_numbers import Solution
from utils.linked_list import create_linked_list, linked_list_to_list

def test_addTwoNumbers():
    solution = Solution()

    assert linked_list_to_list(
        solution.addTwoNumbers(
            create_linked_list([2, 4, 3]),
            create_linked_list([5, 6, 4])
        )
    ) == [7, 0, 8]

    assert linked_list_to_list(
        solution.addTwoNumbers(
            create_linked_list([0]),
            create_linked_list([0])
        )
    ) == [0]

    assert linked_list_to_list(
        solution.addTwoNumbers(
            create_linked_list([9, 9, 9, 9, 9, 9, 9]),
            create_linked_list([9, 9, 9, 9])
        )
    ) == [8, 9, 9, 9, 0, 0, 0, 1]
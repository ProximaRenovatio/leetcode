from solutions.linked_list.medium._0287_find_the_duplicate_number import Solution

def test_find_the_duplicate_number():
    solution = Solution()

    assert solution.findDuplicate([1,3,4,2,2]) == 2
    assert solution.findDuplicate([3,1,3,4,2]) == 3

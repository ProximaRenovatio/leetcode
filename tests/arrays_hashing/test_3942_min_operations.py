from solutions.arrays_hashing.medium._3942_min_operations import Solution as s1
from solutions.arrays_hashing.medium._3942_min_operations_MY_SOLUTION import Solution as s2

def test_minOperations():
    solution1 = s1()
    solution2 = s2()

    assert solution1.minOperations([0,2,1]) == 2
    assert solution1.minOperations([1,0,2]) == 2
    assert solution1.minOperations([2,0,1,3]) == -1
    assert solution1.minOperations([2]) == 0

    assert solution2.minOperations([0,2,1]) == 2
    assert solution2.minOperations([1,0,2]) == 2
    assert solution2.minOperations([2,0,1,3]) == -1
    assert solution2.minOperations([2]) == 0
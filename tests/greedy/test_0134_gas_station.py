from solutions.greedy.medium._0134_gas_station import Solution

def test_gas_station():
    solution = Solution()

    assert solution.canCompleteCircuit(
        [1,2,3,4,5],
        [3,4,5,1,2],
    ) == 3

    assert solution.canCompleteCircuit(
        [2,3,4],
        [3,4,3],
    ) == -1

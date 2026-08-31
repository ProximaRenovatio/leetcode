from solutions.greedy.medium._0763_partition_labels import Solution

def test_partition_labels():
    solution = Solution()

    assert solution.partitionLabels(
        "ababcbacadefegdehijhklij"
    ) == [9,7,8]

    assert solution.partitionLabels("eccbbbbdec") == [10]

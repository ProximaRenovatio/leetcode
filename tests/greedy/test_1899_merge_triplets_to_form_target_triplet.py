from solutions.greedy.medium._1899_merge_triplets_to_form_target_triplet import Solution

def test_merge_triplets_to_form_target_triplet():
    solution = Solution()

    assert solution.mergeTriplets(
        [[2,5,3],[1,8,4],[1,7,5]],
        [2,7,5],
    ) is True

    assert solution.mergeTriplets(
        [[3,4,5],[4,5,6]],
        [3,2,5],
    ) is False

from solutions.stack.medium._1111_max_depth_after_split import Solution

def test_daily_temperatures():
    solution = Solution()

    assert solution.maxDepthAfterSplit("(()())") == [1,0,0,0,0,1]
    assert solution.maxDepthAfterSplit("()(())()") == [1,1,1,0,0,1,1,1]

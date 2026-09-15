from solutions.greedy.hard._2472_max_non_overlapping_palindrome import Solution

def test_maxPalindromes():
    solution = Solution()

    assert solution.maxPalindromes("abaccdbbd",3) == 2
    assert solution.maxPalindromes("adbcda",2) == 0
    assert solution.maxPalindromes("adbcdaasxswpokascmlalaskdjalkcioazkjnxsdjnlaksdenlcasuhajrnflasclasjazijxaspfkoghithnscdjnaksjcnaffasdjkslafffasdafsldjkafsldkjaslfdkjaflskdj",3) == 4

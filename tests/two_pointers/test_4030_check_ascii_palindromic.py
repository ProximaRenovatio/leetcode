from solutions.two_pointers.easy._4030_check_ascii_palindromic import Solution

def test_isPalindromic():
    solution = Solution()

    assert solution.isPalindromic("ff") == True
    assert solution.isPalindromic("leet") == False
    assert solution.isPalindromic("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv") == False
    assert solution.isPalindromic("a") == False
    assert solution.isPalindromic("b") == False

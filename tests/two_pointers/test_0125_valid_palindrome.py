from solutions.two_pointers.easy._0125_valid_palindrome import Solution

def test_valid_palindrome():
    solution = Solution()

    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome(" ") is True

from solutions.two_pointers.medium._0005_longest_palindromic_substring import Solution

def test_longestPalindrome():
    solution = Solution()

    assert solution.longestPalindrome("babad") in ("bab", "aba")
    assert solution.longestPalindrome("cbabdaaab") in ("bab", "aaa")
    assert solution.longestPalindrome("cbabbaaab") == "baaab"

    assert solution.longestPalindrome("abcdcba") == "abcdcba"
    assert solution.longestPalindrome("abcdcbax") == "abcdcba"
    assert solution.longestPalindrome("xabcdcba") == "abcdcba"

    assert solution.longestPalindrome("abcddcba") == "abcddcba"
    assert solution.longestPalindrome("abcddcbax") == "abcddcba"
    assert solution.longestPalindrome("xabcddcba") == "abcddcba"

    assert solution.longestPalindrome("abcddddcba") == "abcddddcba"
    assert solution.longestPalindrome("abcddddcbax") == "abcddddcba"
    assert solution.longestPalindrome("xabcddddcba") == "abcddddcba"

    assert solution.longestPalindrome("abcdddddcba") == "abcdddddcba"
    assert solution.longestPalindrome("abcdddddcbax") == "abcdddddcba"
    assert solution.longestPalindrome("xabcdddddcba") == "abcdddddcba"

    assert solution.longestPalindrome("a") == "a"
    assert solution.longestPalindrome("ab") in ("a","b")
    assert solution.longestPalindrome("aa") == "aa"
    assert solution.longestPalindrome("aab") == "aa"
    assert solution.longestPalindrome("aba") == "aba"
    assert solution.longestPalindrome("baa") == "aa"

    assert solution.longestPalindrome("abbcccba") == "bcccb"
    assert solution.longestPalindrome("ababababa") == "ababababa"

    assert solution.longestPalindrome("tfekavrnnptlawqponffseumswvdtjhrndkkjppgiajjhklqpskuubeyofqwubiiduoylurzlorvnfcibxcjjzvlzfvsvwknjkzwthxxrowidmyudbtquktmyunoltklkdvzplxnpkoiikfijgulbxfxhaxnldvwmzpgaiumnvpdirlrutsqenwtihptnhghobrmmzcsrhqgdgzrvvitzgsolsxjxfeencvpnltxeetmtzlwnhlvgtbhkicivylfjhhfqteyxewmnewhmsnfdyneqoywgsgptwdlzbraksgajciebdchindegdfmayvfkwwkkfyxqjcv") == "kwwk"
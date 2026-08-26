from solutions.strings.medium._0006_zigzag_conversion import Solution

def test_convert():
    solution = Solution()

    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
    assert solution.convert("AB", 1) == "AB"
    assert solution.convert("AB", 2) == "AB"
    assert solution.convert("ABC", 1) == "ABC"
    assert solution.convert("ABC", 2) == "ACB"
    assert solution.convert("ABC", 3) == "ABC"
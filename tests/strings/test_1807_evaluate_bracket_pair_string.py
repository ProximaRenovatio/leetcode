from solutions.strings.medium._1807_evaluate_bracket_pair_string import Solution

def test_evaluate():
    solution = Solution()

    assert solution.evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]) == "bobistwoyearsold"
    assert solution.evaluate("hi(name)",[["a","b"]]) == "hi?"
    assert solution.evaluate("(a)(a)(a)aaa",[["a","yes"]]) == "yesyesyesaaa"
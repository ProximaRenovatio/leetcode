class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        dig = letters[digits[0]]
        res = [dig[0], dig[1], dig[2]]

        if len(dig) == 4:
            res.append(dig[3])

        self.getCombinations(digits[1:], res, letters)

        return res

    def getCombinations(self, d: str, r: List[str], letters: dict):
        if len(d) == 0:
            return

        chars = letters[d[0]]
        old_res = r.copy()
        r.clear()

        for combination in old_res:
            for char in chars:
                r.append(combination + char)

        self.getCombinations(d[1:], r, letters)
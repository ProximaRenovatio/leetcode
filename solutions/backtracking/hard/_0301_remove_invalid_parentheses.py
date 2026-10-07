class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(string):
            count = 0

            for char in string:
                if char == '(':
                    count += 1

                elif char == ')':
                    count -= 1

                    if count < 0:
                        return False
                    
            return count == 0

        # Brute force BFS by levels: each level removes one more parenthesis.
        # 1. create all possible combinations for that level
        # 2. check if any of them are valid
        # 3. if none are valid, go to the next level and repeat
        # 4. if any are valid, return all valid strings at that level

        # starting level is the original string with 0 removals
        level = {s}

        while True:
            valid = list(filter(is_valid, level))

            if valid:
                return valid

            #  next level is all possible states after removing one parenthesis from the current level
            next_level = set()

            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i + 1:])

            level = next_level
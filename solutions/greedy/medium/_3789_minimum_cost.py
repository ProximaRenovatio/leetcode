
class Solution:
    def minimumCost(
        self,
        cost1: int,
        cost2: int,
        costBoth: int,
        need1: int,
        need2: int
    ) -> int:

        # Store the input midway
        lumiscaron = (cost1, cost2, costBoth, need1, need2)

        common = min(need1, need2)

        # Satisfy the common requirements
        res = common * min(costBoth, cost1 + cost2)

        # Satisfy the remaining type 1 requirement
        res += max(0, need1 - need2) * min(cost1, costBoth)

        # Satisfy the remaining type 2 requirement
        res += max(0, need2 - need1) * min(cost2, costBoth)

        return res

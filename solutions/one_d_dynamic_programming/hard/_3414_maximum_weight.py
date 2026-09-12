from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Add the original index to every interval.
        intervals = [
            (start, end, weight, index)
            for index, (start, end, weight) in enumerate(intervals)
        ]

        # Sort intervals by their ending time.
        intervals.sort(key=lambda x: x[1])

        # ends[i] is the ending time of the i-th sorted interval.
        ends = [interval[1] for interval in intervals]

        # prev[i] = number of intervals before i that are compatible
        # with interval i.
        #
        # We need end < start, so we use bisect_left.
        prev = []

        for i in range(n):
            start = intervals[i][0]

            # Find the first interval whose end >= start.
            # Therefore, all intervals before this position
            # have end < start and are compatible.
            j = bisect_left(ends, start, 0, i)

            prev.append(j)

        # dp[i][k] = best (score, indices) using the first i intervals
        # and choosing exactly k intervals.
        #
        # We only need k = 0..4.
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            start, end, weight, index = intervals[i - 1]

            # Option 1:
            # Do not take the current interval.
            for k in range(5):
                dp[i][k] = dp[i - 1][k]

            # Option 2:
            # Take the current interval.
            compatible = prev[i - 1]

            for k in range(1, 5):
                previous_score, previous_indices = dp[compatible][k - 1]

                candidate_score = previous_score + weight
                candidate_indices = tuple(
                    sorted(previous_indices + (index,))
                )

                current_score, current_indices = dp[i][k]

                # Prefer:
                # 1. Higher score
                # 2. Lexicographically smaller indices if scores are equal
                if (
                    candidate_score > current_score
                    or (
                        candidate_score == current_score
                        and candidate_indices < current_indices
                    )
                ):
                    dp[i][k] = (
                        candidate_score,
                        candidate_indices
                    )

        # We can choose at most 4 intervals,
        # so find the best solution among k = 0..4.
        best_score = -1
        best_indices = ()

        for k in range(5):
            score, indices = dp[n][k]

            if (
                score > best_score
                or (
                    score == best_score
                    and indices < best_indices
                )
            ):
                best_score = score
                best_indices = indices

        return list(best_indices)

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = [-1] * 26
        last = [-1] * 26

        # Find the first and last position of every character
        for i, c in enumerate(s):
            x = ord(c) - ord('a')

            if first[x] == -1:
                first[x] = i

            last[x] = i

        intervals = []

        # Try to build a valid interval for every character
        for c in range(26):
            if first[c] == -1:
                continue

            l = first[c]
            r = last[c]
            ok = True

            i = l
            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character starts before our interval
                if first[x] < l:
                    ok = False
                    break

                r = max(r, last[x])
                i += 1

            if ok:
                intervals.append((l, r))

        # Choose intervals that finish as early as possible
        intervals.sort(key=lambda x: x[1])

        ans = []
        last_end = -1

        for l, r in intervals:
            if l > last_end:
                ans.append(s[l:r + 1])
                last_end = r

        return ans
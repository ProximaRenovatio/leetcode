class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        res = 0

        for dx in range(-n + 1, n):
            for dy in range(-n + 1, n):
                overlaps = 0

                for i in range(n):
                    for j in range(n):
                        ni = i + dx
                        nj = j + dy

                        if 0 <= ni < n and 0 <= nj < n:
                            if img1[i][j] == 1 and img2[ni][nj] == 1:
                                overlaps += 1

                res = max(res, overlaps)

        return res
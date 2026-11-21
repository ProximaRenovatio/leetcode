
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
            n = len(parent)
                    children = [[] for _ in range(n)]

                            for i in range(1, n):
                                        children[parent[i]].append(i)

                                                ans = [1] * n
                                                        new_parent = parent[:]
                                                                last_seen = [-1] * 26
                                                                        prev_seen = [-1] * n

                                                                                stack = [(0, 0)]

                                                                                        while stack:
                                                                                                    node, state = stack.pop()
                                                                                                                c = ord(s[node]) - ord('a')

                                                                                                                            if state == 0:
                                                                                                                                            # Enter node: find the closest matching ancestor
                                                                                                                                                            prev_seen[node] = last_seen[c]

                                                                                                                                                                            if last_seen[c] != -1:
                                                                                                                                                                                                new_parent[node] = last_seen[c]

                                                                                                                                                                                                                last_seen[c] = node

                                                                                                                                                                                                                                # Exit event after processing all children
                                                                                                                                                                                                                                                stack.append((node, 1))

                                                                                                                                                                                                                                                                for child in reversed(children[node]):
                                                                                                                                                                                                                                                                                    stack.append((child, 0))

                                                                                                                                                                                                                                                                                                else:
                                                                                                                                                                                                                                                                                                                # Exit node: restore DFS state
                                                                                                                                                                                                                                                                                                                                last_seen[c] = prev_seen[node]

                                                                                                                                                                                                                                                                                                                                                p = new_parent[node]
                                                                                                                                                                                                                                                                                                                                                                if p != -1:
                                                                                                                                                                                                                                                                                                                                                                                    ans[p] += ans[node]

                                                                                                                                                                                                                                                                                                                                                                                            return ans
                                                                                                                                                                                                                                                                                                                                                                                            
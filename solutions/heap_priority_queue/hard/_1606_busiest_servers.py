import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        size = 1
        while size < k:
            size *= 2

        # Segment tree: number of available servers in each range
        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(index: int, value: int) -> None:
            pos = size + index
            tree[pos] = value

            pos //= 2
            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(node: int, left: int, right: int, start: int) -> int:
            # No available server in this range
            if right <= start or tree[node] == 0:
                return -1

            # Leaf node
            if right - left == 1:
                return left if left < k else -1

            mid = (left + right) // 2

            # Search the left subtree first
            result = find_first(2 * node, left, mid, start)

            if result != -1:
                return result

            return find_first(2 * node + 1, mid, right, start)

        busy = []
        counts = [0] * k

        for i in range(len(arrival)):
            current_time = arrival[i]

            # Release servers that have finished
            while busy and busy[0][0] <= current_time:
                finish_time, server = heapq.heappop(busy)
                update(server, 1)

            preferred = i % k

            # Find the first available server >= preferred
            server = find_first(1, 0, size, preferred)

            # Wrap around if necessary
            if server == -1:
                server = find_first(1, 0, size, 0)

            # Drop request if all servers are busy
            if server == -1:
                continue

            # Assign request
            update(server, 0)
            counts[server] += 1

            heapq.heappush(
                busy,
                (current_time + load[i], server)
            )

        max_requests = max(counts)

        return [
            server
            for server in range(k)
            if counts[server] == max_requests
        ]

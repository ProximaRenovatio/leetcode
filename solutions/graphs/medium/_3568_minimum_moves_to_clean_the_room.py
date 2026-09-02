from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Store the position of each piece of litter
        litter = {}

        # Find the starting position
        start = None

        # Number of pieces of litter
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = k
                    k += 1

        # Bitmask where all bits are 1 means that
        # all pieces of litter have been collected
        full_mask = (1 << k) - 1

        # BFS state:
        # (row, column, mask, remaining_energy)
        queue = deque()

        sr, sc = start
        queue.append((sr, sc, 0, energy))

        # best[(row, column, mask)] stores the maximum
        # amount of energy with which we reached this state
        best = {
            (sr, sc, 0): energy
        }

        # Number of moves made so far
        steps = 0

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        # BFS explores the states level by level.
        # Every level represents one additional move.
        while queue:

            # All states currently in the queue belong
            # to the same BFS level.
            for _ in range(len(queue)):

                r, c, mask, e = queue.popleft()

                # If all litter has been collected,
                # this is the minimum number of moves.
                if mask == full_mask:
                    return steps

                # Try the four possible movements
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Check whether the new position is inside the grid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # We cannot move through walls
                    if classroom[nr][nc] == 'X':
                        continue

                    # We need at least one unit of energy to move
                    if e == 0:
                        continue

                    # Moving costs one unit of energy
                    ne = e - 1

                    # By default, the collected-litter mask
                    # stays unchanged
                    nmask = mask

                    # If we move onto a litter cell,
                    # mark that piece of litter as collected
                    if (nr, nc) in litter:
                        idx = litter[(nr, nc)]
                        nmask |= (1 << idx)

                    # If the new cell is a recharge station,
                    # restore the energy to its maximum value
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    key = (nr, nc, nmask)

                    # If we have already reached the same
                    # position with the same collected litter
                    # and with at least as much energy,
                    # this new state is useless.
                    if key in best and best[key] >= ne:
                        continue

                    # This is a better state, so store it
                    best[key] = ne

                    # Add the new state to the BFS queue
                    queue.append((nr, nc, nmask, ne))

            # Move to the next BFS level
            steps += 1

        # If all litter cannot be collected
        return -1
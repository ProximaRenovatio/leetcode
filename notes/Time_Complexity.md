
# O(n²)

1. [[a,b] for a in range(len(nums)) for b in range(len(nums)) if a!=b and nums[a]+nums[b]==target][0]

2. next([a, b] for a, x in enumerate(nums) for b, y in enumerate(nums) if a != b and x + y == target)

3. next([a, b] for a, b in permutations(range(len(nums)), 2) if nums[a] + nums[b] == target)

- lst[0] on lists: Requires that the entire list already be in memory. It is ideal for sequences of known size.
- next() on generators: Calculates or retrieves only the first element requested at that moment, saving memory and initial computation time.
- In problem 0001_two_sum, whether you use `lst[0]` or `next()` makes no difference because there is a strong assumption that there is exactly one result.
- Permutations to eliminate the nested for loop and the check for a != b
- The dictionary-based approach is unbeatable compared to the rest, outperforming them by an order of magnitude.

# O(n)

4. next([i, nums.index(target - x)] for i, x in enumerate(nums) if target - x in nums and nums.index(target - x) != i)



# Choise of data structure

| **You need to implement...** | **Typical data structure** |
| :--- | ---: |
| Is x present? | set |
| x → value  | dict / hash map |
| Index-based access | list / array |
| Always minimum/maximum | heap |
| Sorted data + search | binary search / BST |
| FIFO | queue / deque |
| LIFO | stack |
| Intervals/windows | sliding window + auxiliary structure |



# If the key set is small and well-defined, an array can be used instead of a hash map.
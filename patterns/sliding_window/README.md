# Sliding Window

## When to Use It

- array or string;
- contiguous subarray/substring;
- need to find the maximum, minimum, count, or length;
- there is a condition that must remain valid within the window.

## Conceptual Template

```python
left = 0

for right in range(len(nums)):
    # add nums[right]

    while window_is_invalid:
        # remove nums[left]
        left += 1

    # update the answer
```

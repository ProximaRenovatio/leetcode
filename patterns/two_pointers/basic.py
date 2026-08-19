def two_pointers(nums: list[int]) -> None:
    """Generic two-pointer skeleton for study/reference."""
    left = 0
    right = len(nums) - 1

    while left < right:
        # evaluate nums[left] and nums[right]
        # move one or both pointers
        left += 1
        right -= 1

def binary_search_boundary(left, right, condition):
    while left < right:
        mid = (left + right) // 2

        if condition(mid):
            right = mid
        else:
            left = mid + 1

    return left
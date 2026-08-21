def quick_sort(nums, low, high):
    '''QuickSort is a sorting algorithm based on the Divide and Conquer that 
    picks an element as a pivot and partitions the given numsay around the picked pivot by placing the pivot in its correct position in the sorted numsay'''
    if low >= high:
        return

    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[i], nums[high] = nums[high], nums[i]

    quick_sort(nums, low, i - 1)
    quick_sort(nums, i + 1, high)
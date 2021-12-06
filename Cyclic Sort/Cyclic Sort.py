def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
            continue
        position = nums[i] - 1
        nums[i], nums[position] = nums[position], nums[i]
    return nums


nums = [1, 5, 6, 4, 3, 2]
print(cyclic_sort(nums))

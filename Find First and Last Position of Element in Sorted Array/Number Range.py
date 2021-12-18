def find_range(arr, key):
    result = [- 1, -1]
    start, end = 0, len(arr) - 1
    index = -1

    # Looking for a key in the array with Binary Search technique
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            index = mid
            break
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # If key wasn't found - return [-1, -1]
    if index == -1:
        return result

    # Finding the stating and ending position of the key range
    start = end = index
    while start > 0 and arr[start - 1] == key:
        start -= 1
    while end < len(arr) - 1 and arr[end + 1] == key:
        end += 1

    return [start, end]

'''
#Lower Bound Question:
# 33. Search in Rotated Sorted Array
# 912. Sort an Array 


def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
    return low

print(lower_bound([2, 3, 7, 11, 11, 25], 9))
print(lower_bound([2, 3, 7, 11, 11, 25], 11))
print(lower_bound([2, 3, 7, 11, 11, 25], 100))

'''
#33. Search in Rotated Sorted Array


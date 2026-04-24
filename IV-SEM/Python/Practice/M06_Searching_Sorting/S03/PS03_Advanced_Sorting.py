'''
#Merge Sort
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

print("Enter arrray elements: ")
arr = list(map(int, input().split()))
print(merge_sort(arr))

'''

#Quick Sort
#Identify pivot element index
def Partition(arr, low, high):
    pivot = arr[low]
    i, j = low + 1, high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def Quick_Sort(arr, low, high):
    if low < high:
        p = Partition(arr, low, high)
        Quick_Sort(arr, low, p - 1)
        Quick_Sort(arr, p + 1, high)
    return arr

print("Enter arrray elements: ")
arr = list(map(int, input().split()))
print(Quick_Sort(arr, 0, len(arr) - 1))

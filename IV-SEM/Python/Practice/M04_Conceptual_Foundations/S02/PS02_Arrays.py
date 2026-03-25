'''
1. Reverse the array elements
    a. Using slicing
    b. Using reverse()
    c. Using for loop
2. Check if Array is sorted
3. Find max and min element in the array
4. Find second largest element in the array
5. Remove duplicates in Array
6. Count frequency of elements
7. Rotate Array
8. Leet code problems -> 724


#Using slicing
arr = [1, 2, 3, 4, 5]
print(arr[::-1])

#Using reverse()
arr.reverse()
print(arr)

#Using for loop
arr2 = [1, 2, 3, 4, 5]
res = []
for i in range(len(arr2) - 1, -1, -1):
    res.append(arr2[i])
print(res)

#2 Check if array is sorted
arr3 = [10, 34, 12, 45, 3, 6, 20]
for i in range(len(arr3) - 1):
    if arr3[i] > arr3[i + 1]:
        print("Array is not sorted")
        break
else:    
    print("Array is sorted")   

#3 Find max and min element in the array
arr4 = [10, 34, 12, 45, 3, 6, 20]
print("Max of Array:", max(arr4))
print("Min of Array:", min(arr4))

#Without functions
max1 = arr4[0]
min1 = arr4[0]
for i in range(len(arr4)):
    if arr4[i] > max1:
        max1 = arr4[i]
    if arr4[i] < min1:
        min1 = arr4[i]
print("Max of Array:", max1)
print("Min of Array:", min1)

#4 Find second largest element in the array
arr5 = [10, 34, 12, 45, 3, 6, 20]
arr5.sort()
print("Second Largest Element in Array:", arr5[-2])

#Without function
max1 = arr5[0]
second_max = arr5[0]
for i in range(len(arr5)):
    if arr5[i] > max1:
        second_max = max1
        max1 = arr5[i]
    elif arr5[i] > second_max and arr5[i] != max1:
        second_max = arr5[i]
print("Second Largest Element in Array:", second_max)

#5. Remove duplicates in array
arr6 = [1, 3, 4, 1, 6, 3, 3, 4, 5]
print(list(set(arr6)))

#Without function
res = []
for i in arr6:
    if i not in res:
        res.append(i)
print("Array after removing duplicates:", res)

#6. Count frequency of elements
arr7 = [1, 3, 4, 1, 6, 3, 3, 4, 5]
freq = {}
for i in arr7:
    if i in freq:
        freq[i] += 1 # 1
    else:
        freq[i] = 1
print("Frequency of elements in Array:", freq)


#Countof function
arr7 = [1, 3, 4, 1, 6, 3, 3, 4, 5]
freq = {}
for i in arr7:
    freq[i] = arr7.count(i)
print("Frequency of elements in Array:", freq)

#7. Rotate Array
arr8 = [1, 2, 3, 4, 5]
print("Original Array:", arr8)
#Rotate left by 2
k = 2
res = arr8[k:] + arr8[:k] #[3, 4, 5] + [1, 2]
print("Array after left rotation by 2:", res)

for i in arr8:
    rotated = arr8[k:] + arr8[:k] #[3, 4, 5] + [1, 2]
print("Array after left rotation by 2:", rotated)
'''
#8. Leet code problems -> 724 pivot index else print -1
def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)):
        right = total_sum - left_sum - nums[i]
        if left_sum == right:
            return i
            break
        left_sum += nums[i]
    else:
        return -1
nums = [1, 7, 3, 6, 5, 6]
print("Pivot Index:", pivotIndex(nums))


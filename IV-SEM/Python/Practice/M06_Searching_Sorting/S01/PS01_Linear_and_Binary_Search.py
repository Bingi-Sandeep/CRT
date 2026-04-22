'''
Searching Techniques:
1. Linear Search (Sequential Search)
    Time Complexity: Best Case: O(1)
                     Average Case: O(n)
                     Worst Case: O(n)

2. Binary Search (Interval Search)
    Time Complexity: Best Case: O(1)
                     Average Case: O(log n)
                     Worst Case: O(log n)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Enter List values: ")
l1 = list(map(int, input().split()))
target = int(input("Enter Taget value: "))
print(linear_search([12, 25, 63, 5, 78, 10], 63))
print(linear_search([12, 25, 63, 5, 78, 10], 100)) 
print(linear_search(l1, target))         

'''

def binary_search(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print("Enter List values: ")
l1 = list(map(int, input().split()))
target = int(input("Enter Taget value: "))
print(binary_search(l1, target))

#koko eating bananaes using binary search using with k 
def minEatingSpeed(piles, h):
    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = sum((pile - 1) // mid + 1 for pile in piles)

        if hours > h:
            left = mid + 1
        else:
            right = mid

    return left
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))




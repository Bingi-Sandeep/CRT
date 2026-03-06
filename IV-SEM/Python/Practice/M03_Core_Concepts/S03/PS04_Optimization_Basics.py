'''
Optimization: It is the process of modifying the code to reduce the time complexity.
Brute Force --> Trying of all possible combinations.
Optimal Solution --> Needs thinking, low complexity.

Common ways to optimize code:
1. Time Complexity Optmization --> O(n^2) to O(n)
2. Using hashing (dict, set) to optimize lookups.
3. Avoid redundant calculations (memoization).
4. Use built-in functions and libraries (like sum(), max(), min()).
5. List comprehensions optimization.

Why optimization is important?
1. Improves programs speed.
2. Reduces memory usage.
3. Makes code more efficient.
4. Avoid nested loops.


arr = [10, 20, 30, 40, 50]
for i in range(len(arr)):
    for j in range(len(arr)):
            print(arr[i] + arr[j]) # O(n^2) time complexity

print("Optimized Solution:")
arr = [10, 20, 30, 40, 50]
for num in arr:
    print(num + num) # O(n) time complexity




Programs:
1. FInd the sum of numbers in array.
'''

print("Sum of Numbers in array using Brute force:")
arr = [1, 2, 3, 4, 5]
sum1 = 0
for i in range(len(arr)):
    sum1 += arr[i] #Time Complexity: O(n)
print(sum1)


print("Sum of Numbers in array using optimal solution:")
arr= [1, 2, 3, 4, 5]
print(sum(arr))

#2. Find the square of numbers in array.
print("Square of numbers in array using brute force:")
arr = []
for i in range(10):
    arr.append(i * i)
print(arr)

#2. Find the square of numbers in array using list comprehension.
print("Square of numbers in array using list comprehension:")
print([i * i for i in range(10)])

#2. Find the maximum ele in list
print("Maximum element in the list using brute force:")
arr = [1, 2, 5, 3, 4]

max1 = arr[0]
for num in arr:
    if num > max1:
        max1 = num

print(max1) #Time Complexity: O(n)

print("Maximum element in the list optimal way:")
arr = [1, 2, 3, 4, 5]
print(max(arr)) #Time Complexity: O(n)


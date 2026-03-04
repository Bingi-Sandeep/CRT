'''
1. Find Largest Number (Using max() function)
2. Check Palindrome (Using reversed() and join() functions)
3. Count Even Numbers (Using filter()).
4. Remove Duplicates (Using set())
5. Sum of Digits (Using sum())
6. Sort words alphabetically (Using sorted())
7. Find common elements (using set())
8. Index with value (Using enumerate())
9. Pair two lists (Using zip())
10. Find Second Largest Number (Using sorted())
'''
#1 Finding the largest number in a list using max() function
arr = [10, 23, 54, 85, 10, 25]
print("Max of arr:", max(arr))  # Output: 85

#2 Using reversed() and join() functions to check if a string is a palindrome
word = "madam"
if word == "".join(reversed(word)):
    print("Palindrome")
else:
    print("Not a palindrome.")

#3 Using filter() function to count even numbers in a list
arr = [10, 7, 45, 68, 45, 24]
res = list(filter(lambda x : x % 2 == 0, arr))
print("Even Count:", res)

#4 Removing duplicates from a list using set() function
arr = [1, 2, 4, 3, 2, 1, 4 ,3]
print("Original Array:", arr)
print("After removing duplicates:", list(set(arr)))

#5 Sum of digits using sum() function
arr = [1, 2, 3, 4]
print("Sum of digits:",sum(arr))

#6 Alphabetical order of words using sorted() function
arr = ['A', 'Z', 'C', 'L', 'D', 'B']
print("Alphabetical Order:", sorted(arr))

#7 Common elements in two lists using set() and intersection() functions
arr1 = [1, 2, 4, 5, 3]
arr2 = [2, 3, 6, 7, 5]
a = set(arr1)
b = set(arr2)
print("Common elements:", a.intersection(b))

#8 Enumerate() function to get index and value from a list
arr = [20, 54, 45, 68, 45, 24]
for i, val in enumerate(arr):
    print(f"Index: {i}, Value: {val}")

#9 Pairing two lists using zip() function
arr1 = ['A', 'B', 'C']
arr2 = [1, 2, 3]
paired = list(zip(arr1, arr2))
print("Paired List:", paired)

#10 Finding the second largest number in a list using sorted() function
arr = [10, 23, 54, 85, 10, 25]
sorted_arr = sorted(arr, reverse=True)
print("Second Largest Number:", sorted_arr[1])
'''
Set:
1. Use {} to create a set.
2. Set does not allow duplicate values.
3. Set is unindexed.
4. Set is unordered.
5. Set is heterogeneous.
6. Set is mutable.



s = {1, True, 10, 12.45, 10, 9 + 5j}  # 1 is treart as True, 0 is treated as False
print(s, type(s))

#Adding elements
A = {1, 2, 3}
B = {3, 4, 5}

A.add(4)
B.update({6, 7})

print(A, B)

#Remove elements
A.pop()
print("After pop() fn: ", A)


#Leetcode prob: 268 Missing number
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

def missingNumber(nums):
    ran = len(nums)
    for i in range(ran + 1):
        if i not in nums:
            return i
        
#Main
nums = list(map(int,input("Enter List Items: ").split()))
print(missingNumber(nums))



#Diff Method
nums = [3, 0, 1]
n = len(nums)
res = set(range(n + 1))
print(*(res - set(nums)))

s = (n * (n + 1)) // 2
print(s - sum(nums))



349. Intersection of Two Arrays
Given two integer arrays nums1 and nums2,
return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

nums1 = list(map(int, input("Enter List one Items: ").split()))
nums2 = list(map(int, input("Enter List two Items: ").split()))

s1 = set(nums1)
s2 = set(nums2)

print(s1.intersection(s2))


Tuples:
1. Definition: It is a ordered and immutable collection of data.
2. Symbol: It is represented by parentheses ().
3. Accesing: INdex positions +ve or -ve.
4. Concatenation: + operator.
5. Nesting of tuples: tuple inside tuple.
6. Repeation of tuples: * operator.
7. Slicing of tuples: [start:stop:step]
8. Deletion of tuples: del keyword.
9. Leetcode Problems on Tuples (349, 657)

t1 = (10, 20, 30, 40)
t2 = ("Sandeep", "Python", "Programming")
print("Index:t1[0]:", t1[0])
print("t1[-1]:", t1[-1])
print("Concatenation: ", t1 + t2)
print("t1, t2:", t1, t2)
print("Repeated tuple:", t1 * 5)
print("Slicing: ", t1[1:4])
print("t1[:5]:", t1[:5])
print("Reverse:", t1[::-1])

del t1 # Deleting the tuple t1
#print(t1)   NameError: name 't1' is not defined


#Leetcode Problem: 657 Robot return to origin

moves = input("Enter Moves: ")
x = 0
y = 0

for move in moves:
    if move == "R":
        x += 1
    elif move == "L":
        x -= 1
    elif move == "U":
        y += 1
    elif move == "D":
        y -= 1

if x == 0 and y == 0:
    print(True)
else:
    print(False)


#Leetcode Problem: 238 Product of Array Except Self
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
          #Write your code here
          ans = []
          
          for i in range(len(nums)):
              p = 1
              for j in range(len(nums)):
                  if i != j:
                      p *= nums[j]
              ans.append(p)
          return ans

#Main
nums = list(map(int, input("Enter List Items: ").split()))
s = Solution()
print(s.productExceptSelf(nums))



Dictionary:

1. Definition: It is an unordered collection of key-value pairs.
2. Craetion ({} or dict() fn).
3. Accessing dict items (keys).
4. Adding & Updating dict items (assignment)
5. 
'''
d = {"Name": "Sandeep", "Age": 20, "City": "Hyderabad"} #Using {}
print(d) 

d2 = dict(Name="Sandeep", Age=20, City="Hyderabad") #Using dict() fn with keyword arguments
print(d2)
print(d2["Name"]) #Accessing dict items (keys)
print(d2.get("Age")) #Using get() fn to access dict items
print(d2.keys()) #Getting all keys
print(d2.values()) #Getting all values
d2['Hobby'] = 'Gaming' #Adding new key-value pair 
print(d2)

'''
Delete dict items:
1. Using del keyword. del-->Deletes the entire dictionary or specific key-value pair.
2. Using pop() fn. pop() --> Removes last inserted key-value pair 
3. popitem() fn. popitem() --> Removes the last inserted key-value pair and returns it as a tuple.
4. clear() fn. clear() --> Removes all items from the dictionary, leaving it empty.
242
'''
#Leetcode Problem: 1 Two Sum Using Dictionary
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in d:
            return [d[complement], i]
        d[nums[i]] = i


#Main
nums = list(map(int, input("Enter List Items: ").split()))
target = int(input("Enter Target: "))
print(twoSum(nums, target))
        
#Array recursion
'''
Recursion with Lists and Strings
Example
1. Calculate the sum of all elements in a list
2. Reverse a List 
3. Reverse a String
4. check palindrome
'''

#Calculate the sum of all elements in a list
def Array_Sum(nums):
    s = 0
    stop = -1 * (len(nums)+1)
    for i in range(-1,stop,-1):
        s += nums[i]
    return s

print(Array_Sum([10,20,30,40]))#100

def Array_Sum1(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[-1] + Array_Sum1(nums[:-1])
    
print(Array_Sum1([10,20,30,40]))#100

#Reverse a List 
def Reverse_Array(nums,i,j):
    if i >= j:
        return
    nums[i],nums[j] = nums[j],nums[i]
    Reverse_Array(nums,i+1,j-1)
    return nums

print(Reverse_Array([1,2,3,4,5],0,4))#[5,4,3,2,1]

#Reverse a String
def Reverse_str(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + Reverse_str(s[:-1])
    
def is_palindrome(s):
    return s == Reverse_str(s)

print(Reverse_str("python")) #"nohtyp"
print(is_palindrome("abc")) #False
print(is_palindrome("madam")) #True
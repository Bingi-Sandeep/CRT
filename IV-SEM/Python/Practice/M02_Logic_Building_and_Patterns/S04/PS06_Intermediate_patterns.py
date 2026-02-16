'''
li = [1, 2, 3, 4, 5]
#Output: [2, 4, 6, 8, 10]
res = []
for val in li:
    res.append(val * 2)
print(res)

print([val * 2 for val in li])

#Print even numbers
li = list(map(int, input("Enter List:").split()))
res = []
for val in li:
    if val % 2 == 0:
        res.append(val)
print(res)

print([val for val in li if val % 2 == 0])
print(tuple(val for val in li if val % 2 == 0))
print({val:val * 2 for val in li if val % 2 == 0})


#.join method
#Basic joining 
li = ['a', 'b', 'c']
res = ""
for val in li:
    res = res + val + " "
print("Using separate string variable: ", res)
print("Using * : ", *li)

#Using .join
print("Using .join: "," ".join(li))


#1. Pyramid
#Input: 4
#Output:
   *
  * *
  * * *
* * * *

n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    for _ in range(n - i):
        print(" ", end = "")
    for j in range(i):
        print("*", end = " ")
    print()

n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + " * " * i)

#Diamond Pattern
#Input: 3
#Output:
  *
 * *
* * *
 * *
  *


n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
'''

#Palindrome Pattern
n = int(input("Enter number of rows: "))
for i in range(n):
    print(" ".join(str(j) for j in range(i + 1, 0, -1)) + " " + " ".join(str(j) for j in range(2, i + 2)))
    #print(" ".join(str(j)for j in range(n, 0, -1))] + " ".join(str(j)for j in range(2, n)))
  



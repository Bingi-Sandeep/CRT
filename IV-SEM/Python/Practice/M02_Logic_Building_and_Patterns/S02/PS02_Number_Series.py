'''
#Number Series: Sequential order of numbers in a specific pattern

# 1. Print n natural numbers

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i, end = ' ')

    
# 2. Print n even numbers

n = int(input("Enter a number: "))
for i in range(2, n + 1, 2):
    print(i, end = ' ')

    
# 3. Print n odd numbers

n = int(input("Enter a number: "))
for i in range(1, n + 1, 2):
    print(i, end = ' ')


# 4. Print n Fibonacci numbers

n = int(input("Enter a number: "))
a, b = 0, 1

for i in range(n):
    print(a, end = ' ')
    a, b = b, a + b

OR:

n = int(input("Enter a number: "))
count = 0
while count < n:
    print(a, end = ' ')
    a, b = b, a + b
    count += 1


# 5. Print Multiplication Table of a given number

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

OR: 

n = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1



# 6. Print squares of first n natural numbers

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i ** 2, end = ' ')


# 7. Print cubes of first n natural numbers

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i ** 3, end = ' ')



# Alternative Series
# 1. Print 1, -2, 3, -4, 5, -6, ...

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(-i, end = ' ')
    else:
        print(i, end = ' ')


# 2. Print -1, 2, -3, 4, -5, 6, ...

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end = ' ')
    else:
        print(-i, end = ' ')

print()

# 3. Print 1, 2, 4, 7, 11, 16, ...
n = int(input("Enter a number: "))
a = 1
for i in range(n):
    print(a, end = ' ')
    a += i + 1

'''
# 4. 1, 2, 6, 24, 120, ...

n = int(input("Enter a number: "))
a = 1
for i in range(1, n + 1):
    a *= i
    print(a, end = ' ')



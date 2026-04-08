'''
#Sum of n natural numbers
#Traditional way:
def Natural_Sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
#Using Recursion:
def Natural_Sum1(n):
    if n == 1:
        return 1
    else:
        return n + Natural_Sum(n-1)
        
print(Natural_Sum(10))
print(Natural_Sum1(10)) 

#Factorial of a number
#Traditional way:
def Factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(Factorial(5))
print(Factorial(10))

#Using Recursion:
def Factorial1(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial1(n-1)
print(Factorial1(5))
print(Factorial1(10))


#Fibonacci series nth term:
#Traditional way:
def Fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
print(Fibonacci(5))
   
#Using Recursion:
def Fibonacci1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci1(n-1) + Fibonacci1(n-2)
print(Fibonacci1(5))
'''

#GCD of two numbers:
#Traditional way:
def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

print(GCD(12, 8))

#Using Recursion:
def GCD1(a, b):
    if b == 0:
        return a
    else:
        return GCD1(b, a % b)
print(GCD1(12, 8))

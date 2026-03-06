'''
Math Basics in Python

1. Basic arithmetic operations: +, -, *, /, //, %, **.
2. Built-in functions: abs(), round(), pow(), max(), min().
3. Math library functions: math.sqrt(), math.floor(),  math.log(), math.ceil() etc.

#Write python code to print all arithmetic opearators (+, -, *, /, //, %, **).

a = 10
b = 5
print("Arithemetic Operators:")
print("a =", a, "b =", b)
print("+ Operaotor:", a + b)
print("- Operaotor:", a - b)
print("* Operaotor:", a * b)
print("/ Operaotor:", a / b)
print("// Operaotor:", a // b)
print("% Operaotor:", a % b)
print("** Operaotor:", a ** b)
print()

#Write python code to print all built-in functions (abs(), round(), pow(), max(), min()).
print("Built-in functions:")
print("Absolute value of -5:", abs(-5))
print("Round value of 3.14:", round(3.14))
print("Power of 2^3:", pow(2, 3))
print("Maximum value in list:", max([1, 2, 9, 4, 5]))
print("Minimum value in list:", min([1, 2, 8, 4, 5]))
print("Sum of list:", sum([1, 2, 3]))
print()
#Using Math module
print("Using Math Module:")

import math
print("Square root of 81:", math.sqrt(81))
print("Ceiling of 4.2:", math.ceil(4.2)) #Returns the smallest integer greater than or equal to 4.2, which is 5.
print("Floor of 4.2:", math.floor(4.2)) #Returns the largest integer less than or equal to 4.2, which is 4.
print("Value of π:", math.pi)
print("Factorial of 6:", math.factorial(6))

#1. Find the GCD using math module and using Euclidean meythod.
import math
print("GCD using math module:")
print(math.gcd(48, 18))
print()

print("GCD using Euclidean method:")
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(gcd(a, b))


#2. Find LCM of tow numbers.
print("LCM of two numbers:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = (a * b) // gcd(a, b)
print("LCM of", a, "and", b, "is:", lcm)

#Without using GCD
print("LCM of two numbers without using GCD:")
lcm = max(a, b)
while lcm % a != 0 or lcm % b != 0:
    lcm += max(a, b)
print("LCM of", a, "and", b, "is:", lcm)

  
'''
#3. Write a python code to check a number is perfect number or not.
print("Check if a number is perfect number or not:")
num = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
if sum_of_divisors == num:
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")



  
        
       
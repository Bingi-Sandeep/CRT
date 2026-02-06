'''
1. Write a python code for the factorialof a number


n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is", factorial)


#2. Write a python code to check whether a number iss Armstrong number or not?
#Ex: 153 --> 1^3 + 5^3 + 3^3 = 153
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


#3. Write a python code to check whether a number is Prime or not?
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

#4. Print Prime Numbers in a given range
n = int(input("Enter the upper limit: "))
print("Prime numbers between 1 and", n, "are:") 
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
Code Explanation for prime with range:
1. The user is prompted to enter an upper limit for the range of prime numbers.
2. A loop iterates through numbers starting from 2 up to the upper limit (inclusive).
3. For each number, a flag `is_prime` is set to True initially.
4. Another loop checks if the current number is divisible by any number from 2 to the square root of the current number.
5. If the current number is divisible by any of those numbers, `is_prime` is set to False, and the inner loop breaks.
6. After the inner loop, if `is_prime` remains True, it means the current number is prime, and it is printed to the console.



#5. Monotonic of an Array
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False
    return increasing or decreasing
arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
if is_monotonic(arr):
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")

#6. Reverse Integer with signed 32 bit integer range [-2^31, 2^31 - 1] then return 0

def reverse_integer(n):
    sign = -1 if n < 0 else 1
    n *= sign
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    reversed_num *= sign
    if -2**31 <= reversed_num <= 2**31 - 1:
        return reversed_num
    else:
        return 0

num = int(input("Enter an integer: "))
print("Reversed integer:", reverse_integer(num))


#7. Roman to Integer

def roman_to_integer(s):
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(s):
       if roman_numerals[char] < prev_value:
            total -= roman_numerals[char]
       else:
           total += roman_numerals[char]
           prev_value = roman_numerals[char]
    return total
roman = input("Enter a Roman numeral: ").upper()
print("Integer value:", roman_to_integer(roman))

'''
#8. Happy Number
#Ex: 19 --> 1^2 + 9^2 = 82 --> 8^2 + 2^2 = 68 --> 6^2 + 8^2 = 100 --> 1^2 + 0^2 + 0^2 = 1 (Happy Number)
num = int(input("Enter a number: "))
seen = set()
while num != 1 and num not in seen:
    seen.add(num)
    sum_sq = 0
    while num > 0:
        dgt = num % 10
        sum_sq += dgt * dgt
        num //= 10
    num = sum_sq
if num == 1:
    print("The number is a happy number.")
else:
    print("The number is not a happy number.")

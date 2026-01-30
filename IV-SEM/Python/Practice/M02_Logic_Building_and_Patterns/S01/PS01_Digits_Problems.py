#1. Count the number of digits in a number
'''
n = 1524

n % 10 ==> last digit

n // 10 ==> quotient number without last digit

n = int(input())
temp = n
counter = 0

while n > 0:
    counter += 1
    n //= 10
print(counter) or print(len(str(temp)))


# 2.Sum of digits

n = int(input())

s = 0
while n > 0:
    digit = n % 10
    s += digit
    n //= 10
print(s)

#3. count odd and even digits
n = int(input())

odd = 0
even = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print("Even:", even)
print("Odd:", odd)


# 4. Sum the digits of number until signle digit

n = int(input())

while n > 10:
    s = 0
    while n > 0:
        digit = n % 10 
        s += digit
        n //= 10
    n = s
print(s)
'''
# OR

n = int(input())
while n > 10:
    n = sum(list(map(int, str(n))))
print(n)
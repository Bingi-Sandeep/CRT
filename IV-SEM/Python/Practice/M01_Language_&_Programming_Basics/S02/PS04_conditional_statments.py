n = int(input())
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
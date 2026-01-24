digits = [9]
n = 0
for i in digits:
    n = (n*10) + i
print(n)
n = n+1
res = []
while n > 0:
    res.insert(0,n%10)
    n //= 10
print(res)
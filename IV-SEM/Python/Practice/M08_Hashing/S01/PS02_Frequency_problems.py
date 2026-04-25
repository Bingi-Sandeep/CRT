'''
Frequency of each element in array
[1, 2, 4, 5, 2, 3, 1, 1] ==> {1:3, 2:2, 3:1, 4:1, 5:1}

print("Enter List: ")
l1 = list(map(int, input().split()))

dict = {}

for i in l1:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print(dict)

d1 = {}
for val in l1:
    d1[val] = d1.get(val, 0) + 1
print(d1)
print(max(d1.key()))
'''
#Print Max frequency
from collections import Counter
li = list(map(int, input().split()))
freq = dict(Counter(li))
print(max(freq, key = freq.get))
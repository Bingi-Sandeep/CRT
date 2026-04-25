'''
Hasing Types:
1. Linear Probing
2. Quadratic Probing
3. Double hashing

Set: Duplicates are not allowed.
'''
#Set
s = set()

#Dictionary
d = {}

#Adding entries
d[1] = 'a'
d.update({2:'b', 3:'c'})
d.setdefault(4,'d')

#Fetch value
print(d.get(5, "Not Found"))

print(d.keys())
print(d.values())
print(d.items())
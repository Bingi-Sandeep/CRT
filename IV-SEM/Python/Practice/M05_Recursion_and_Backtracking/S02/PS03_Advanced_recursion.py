'''
1. Digital Root using Recursion
2. Check if Array is Sorted using Recursion
'''
#Digital Root using Recursion
def Digital_Root(n):
    if n < 10:
        return n
    s = sum([int(i) for i in str(n)])
    return Digital_Root(s)

print(Digital_Root(245))#2

#Check if Array is Sorted using Recursion
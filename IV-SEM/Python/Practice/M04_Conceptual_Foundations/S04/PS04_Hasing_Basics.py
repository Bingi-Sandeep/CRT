# Frequency Count of Elements in an Array
def frequency_count(s):
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1 
        else:
            freq[i] = 1
    return freq

s = input("Enter a string: ")
freq = frequency_count(s)
print("Frequency of elements in Array:", freq)

#Using dict
s = input("Enter a string: ")
freq = {}
for i in s:
    freq[i] = freq.get(i, 0) + 1
print("Frequency of elements in Array:", freq)

#Leetcode problems
'''
1.Two sums(#1)
2.Contains Duplicate(#217)
3.Valid anagram(#242)
4.Happy number(#202)
5.First unique character in a string(#387)

'''


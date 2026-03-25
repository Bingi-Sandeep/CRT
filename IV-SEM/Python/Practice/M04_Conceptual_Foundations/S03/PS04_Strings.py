"""
String
String is a collection of characters enclosed in single quotes.
String is immutable.




s = "python"
s1 = 'Python'
s2 = '''
Python is a programming language.
'''
print(s + s1) #Concatenation
print(s * 2) #Repetition
print("on" in s1)

# s[1] = 'a' -> Error, String is immutable
#Built-in Functions
print(len(s))
print(max(s))
print(min(s))
print(max("abc123ABC")) #c = 99, C = 67, a = 97, A = 65

#Built-in Methods
print(s.upper())
print(s.lower())
s5 = s.replace("y", "Y")
print(s5)
s4 = "   Hello World!   "
print(s4.strip())
print(s)

#print(dir(str)) -> List of all built-in methods for string

print(s.find("on"))
print(s.find("xyz")) #Returns -1 if substring is not found

#Reverse a string without using slice range
s = input("Enter a string: ")
res = ""
for i in range(len(s) - 1, -1, -1):
    res += s[i]
if res == s:
    print("Is Palindrome")
else:
    print("Not a Palindrome")
"""
#Anagram without using in-built fn
s1 = input("Enter First string: ")
s2 = input("Enter Second string: ")
is_angrm = False
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            is_angrm = True
            break
    if not is_angrm:
        break
print("Is Anagram" if is_angrm else "Not a Anagram")

#Using Counter
from collections import Counter
print("Is Anagram" if Counter(s1) == Counter(s2) else "Not a anagram")
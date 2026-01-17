'''
Data Types:
1. fundamental data types:
    a.int
    b.float
    c.boolean
    d.complex
    e.string
2. Collection data types:
    a.list
    b.tuple
    c.set
    d.dictionary

'''
x = 12
y = 12.34
z = 4 + 3
a = True
b = "Hello World"

print(x, type(x))
print(y, type(y))
print(z, type(z))
print(a, type(a))
print(b, type(b))

f1 = 3e2
f2 = 4E3

print(f1, type(f1))
print(f2, type(f2))

c1 = 4 + 5j
c2 = complex(2, -3)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

print(c1.real)
print(c2.imag)

s = "python"
print(s[2])
print(s[::])
print(s[::2])
print(s[::-1])
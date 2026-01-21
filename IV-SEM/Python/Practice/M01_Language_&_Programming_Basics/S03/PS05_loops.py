'''
n = 65
counter = 0
while n > 0:
    counter += 1
    n //= 10
print(counter)

#Print Hello world! 5 times using for loop
counter = 0
while counter<5:
    print("Hello World!")
    counter+=1
for counter in range(0,5,1):
    print("Hello World!")

l1 = [1, 2, 3, 4, 5]
for i in range(0, len(l1)):
    l1[i] = l1[i] ** 2
print(l1)

l2 = [1, 2, 3, 4, 5]
for v in l2:
    if v % 2 == 0:
        print(v, end = " ")

s = input()
counter = 0
for v in s:
    if v in "aeiouAEIOU":
        counter += 1
print(counter)

for i in range(1,11):
    if i ==5:
        break
    print(i,end=" ")
    Password retry system (max 3 attempts)
    If password is correct show login successful 
    else attempts exceed show account locked.
'''

for i in range(1,4):
    password = input("Enter Password:")
    crct_pass = "sunny@9985"
    if password == crct_pass:
        print("Correct Password")
        print("Login Successful!")
        break
    else:
        print("Incorrect Password")
        print("You have more ", i, " attempts.")
        continue
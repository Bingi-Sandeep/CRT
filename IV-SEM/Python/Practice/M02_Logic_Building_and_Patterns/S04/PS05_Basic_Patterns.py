'''
#1. Square Star Pattern
n = int(input("Enter the number of rows: "))
for i in range(n): #Rows
    for j in range(n): #Cols
        print("*", end=" ")
    print()

#2. Right-Angled Triangle Star Pattern
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1): #Rows 
    for j in range(i): #Cols
        print("*", end=" ")
    print()

#3. Inverted Right-Angled Triangle Star Pattern
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):           
    for j in range(i):              
        print("*", end=" ")         
    print()

#3.5 Inverted Right-Angled Triangle Star Pattern with minus 1
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):           
    for j in range(i):              
        print("*", end=" ")         
    print()

#4. Number Triangle
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()   
  
#5. Repeated Number Pattern
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = " ")
    print()

#6. Alphabet Pattern
#Input: 5
#Output:
#A
#A B
#A B C
#A B C D
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end = " ")
    print()

#7. Floyd Triangle
n = int(input("Enter the number of rows: "))
var = 1
for i in range(1, n + 1):
    for j in range(i):
        print(var, end = " ")
        var += 1
    print()


#8. Hollow square
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
           
       

#9. Stair Case Pattern or Right-Angled Triangle Star Pattern with spaces
Input: 4
Output:
   *
  **
 ***
****
'''
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end = "")
    for j in range(i):
        print("*", end = "")
    print()



 


   
  









'''
1.Pascal Triangle (in single line)

Input: 5
Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1


Code:

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    c = 1
    for j in range(1, i + 1):
        print(c, end = " ")
        c = c * (i - j) // j
    print()

input = 5
Iteration 1: 1 c = 1 * (1 - 1) // 1 = 0, i = 1, j = 1

Iteration 2: 1 c = 1 * (2 - 1) // 1 = 1 i = 2, j = 1
Iteration 3: 1 c = 1 * (2 - 2) // 2 = 0 i = 2, j = 2

Iteration 4: 1 c = 1 * (3 - 1) // 1 = 2 i = 3, j = 1
Iteration 5: 2 c = 2 * (3 - 2) // 2 = 1 i = 3, j = 2
Iteration 6: 1 c = 1 * (3 - 3) // 3 = 0 i = 3, j = 3

Iteration 7: 1 c = 1 * (4 - 1) // 1 = 3 i = 4, j = 1
Iteration 8: 3 c = 3 * (4 - 2) // 2 = 3 i = 4, j = 2
Iteration 9: 3 c = 3 * (4 - 3) // 3 = 1 i = 4, j = 3
Iteration 10: 1 c = 1 * (4 - 4) // 4 = 0 i = 4, j = 4

Iteration 11: 1 c = 1 * (5 - 1) // 1 = 4 i = 5, j = 1
Iteration 12: 4 c = 4 * (5 - 2) // 2 = 6 i = 5, j = 2
Iteration 13: 6 c = 6 * (5 - 3) // 3 = 4 i = 5, j = 3
Iteration 14: 4 c = 4 * (5 - 4) // 4 = 1 i = 5, j = 4
Iteration 15: 1 c = 1 * (5 - 5) // 5 = 0 i = 5, j = 5




#2. Butterfly Pattern
Input: 4
Output:
*      * 6
**    ** 4
***  *** 2
********
********
***  ***
**    **
*      *

Code:

n = int(input("Enter the size of the butterfly pattern: "))

for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


    
#3. HourGlass pattern 
Input: 4
Output:
* * * *
* * *
* *
*
* *
* * *
* * * *


n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print("* " * i)
for i in range(2, n + 1):
    print("* " * i)

    
#4. Spiral Matrix
Input: 3
Output:
1 2 3
8 9 4
7 6 5

Input: 4
Output:
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7


n = int(input("Enter the size of the spiral matrix: ")) 
spiral_matrix = [[0] * n for _ in range(n)]
num = 1
top, bottom, left, right = 0, n - 1, 0, n - 1
while num <= n * n:
    for i in range(left, right + 1):
        spiral_matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        spiral_matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left - 1, -1):
        spiral_matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        spiral_matrix[i][left] = num
        num += 1
    left += 1
for row in spiral_matrix:
    print(" ".join(map(str, row)))



'''

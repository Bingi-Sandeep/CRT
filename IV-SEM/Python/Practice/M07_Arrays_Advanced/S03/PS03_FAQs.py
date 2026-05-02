
#54 Spiral Matrix
def spiral_matrix(matrix):
    res = []

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            res.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
        bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
        left += 1
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))

#118 Pascal's Triangle
def pascal_triangle(n):
    res = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res
n = 5
print(pascal_triangle(n))
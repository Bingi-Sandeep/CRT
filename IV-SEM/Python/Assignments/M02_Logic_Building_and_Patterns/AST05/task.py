def number_triangle(n: int) -> str:
    res = []
    for i in range(1, n + 1):
        res.append("".join(str(j) for j in range(1, i + 1)))
    return "\n".join(res)

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))
def reverse_number(n: int) -> int:
    res = []
    for _ in range(len(str(n)) - 1, -1, -1):
        res.append(str(n)[_])
    return int("".join(res))
        

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
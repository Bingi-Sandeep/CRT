def sum_of_digits(n: int) -> int:
    sum1 = 0
    while n > 0:
        sum1 += n % 10
        n //= 10
    return sum1

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
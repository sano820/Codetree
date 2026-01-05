a, b = map(int, input().split())

# Please write your code here.
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum_even(n: int) -> bool:
    return sum(int(c) for c in str(n)) % 2 == 0 
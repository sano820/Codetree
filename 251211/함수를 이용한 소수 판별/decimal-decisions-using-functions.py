a, b = map(int, input().split())

# Please write your code here.
def p(n):
    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

def sol(a, b):
    if a > b:
        a, b = b, a
    return sum(x for x in range(a, b + 1) if p(x))

print(sol(a,b))
N = int(input())

# Please write your code here.

def sol(n):
    if n == 1:
        return 1
    else:
        return n + sol(n-1)

print(sol(N))
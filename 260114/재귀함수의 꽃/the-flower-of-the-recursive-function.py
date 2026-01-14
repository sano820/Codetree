N = int(input())

# Please write your code here.
def sol(n):
    n -= 1
    if n == -1:
        return
    print(n+1, end = ' ')
    sol(n)
    print(n+1, end = ' ')

sol(N)

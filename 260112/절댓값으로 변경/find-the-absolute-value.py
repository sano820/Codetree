n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def sol(a):
    if a < 0:
        a *= -1
    return a

for a in arr:
    print(sol(a), end = ' ')

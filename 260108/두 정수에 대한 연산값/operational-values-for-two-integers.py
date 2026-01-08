a, b = map(int, input().split())

# Please write your code here.
def sol(a,b):
    if a < b:
        a *= 2
        b +=25
    else:
        a += 25
        b *= 2
    return a, b

print(sol(a,b)[0], sol(a,b)[1])
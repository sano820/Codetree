n = int(input())

# Please write your code here.
def sol(n):
    a = n//10
    b = n%10
    if n%2==0 and (a+b)%5==0:
        print("Yes")
    else:
        print("No")

sol(n)
n = int(input())

# Please write your code here.

def solutions(n):
    answer = 0
    for i in range(1,n+1):
        answer += i

    print(answer//10)

solutions(n)    
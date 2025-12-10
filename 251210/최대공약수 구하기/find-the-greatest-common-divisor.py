a,b = map(int, input().split())

# Please write your code here.
def solution(a,b):

    while b != 0:
        a, b = b, a % b
    return abs(a)  
print(solution(a,b))
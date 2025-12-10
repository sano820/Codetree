n, m = map(int, input().split())

# Please write your code here.
def gcd(a, b):
    """두 정수 a, b의 최대공약수를 반환"""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def solution(a,b):
    if a == 0 or b == 0:
        return 0   
    return abs(a * b) // gcd(a, b)

print(solution(n,m))
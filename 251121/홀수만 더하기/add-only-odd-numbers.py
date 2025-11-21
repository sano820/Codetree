answer = 0
N = int(input())
for _ in range(N):
    a = int(input())
    if a %2!=0 and a%3==0:
        answer += a
print(answer)
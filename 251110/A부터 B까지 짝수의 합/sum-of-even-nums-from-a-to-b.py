A, B = map(int, input().split())
answer = 0
for i in range(A, B+1):
    if i % 2 ==0:
        answer += i
print(answer)
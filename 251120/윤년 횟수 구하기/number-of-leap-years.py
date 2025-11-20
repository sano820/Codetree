N = int(input())
answer = 0
for i in range(1,N+1):
    if i % 4 ==0:
        if i % 100 ==0 and i % 400 != 0:
            continue
        else:
            answer += 1
print(answer) 
answer = 0
for _ in range(10):
    a = int(input())
    if a % 3 == 0 or a % 5 ==0:
        answer += 1
print(answer)
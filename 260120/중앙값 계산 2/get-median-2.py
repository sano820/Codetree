n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if (i+1) % 2 != 0:
        answer = sorted(arr[0:i+1])
        print(answer)
        # print(answer[len(answer)//2], end = '')
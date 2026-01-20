n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def cal(n:list) -> int:
    answer = []
    sorted_list = sorted(n)
    for i in range(len(n)):
        answer.append(sorted_list[i]+sorted_list[len(n)-i-1])
    return max(answer)

print(cal(nums))
nums = list(map(int, input().split()))

valid_nums = []
for n in nums:
    if n == 0:
        break
    valid_nums.append(n)

for i in range(len(valid_nums)-1,-1,-1):
    print(valid_nums[i], end = ' ')
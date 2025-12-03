nums = list(map(int, input().split()))

valid_nums = []
for n in nums:
    if n == 260:
        break
    valid_nums.append(n)

a = sum(valid_nums)
b = a / len(valid_nums)

print(a, b)
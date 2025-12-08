nums = list(map(int, input().split()))

a ,b = 0, 0
for i in range(0,10,2):
    a += nums[i]

for j in range(1,10,2):
    b += nums[j]

print(b-a)
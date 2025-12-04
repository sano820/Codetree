nums = list(map(int,input().split()))

a = sum(nums[i] for i in range(1,10,2))
b = sum(nums[i] for i in range(2,10,3))/3
print(a, round(b,1))
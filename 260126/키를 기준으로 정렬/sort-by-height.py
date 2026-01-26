n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

idx = sorted(range(n), key=lambda i: height[i])

for i in idx:
    print(name[i], height[i], weight[i])
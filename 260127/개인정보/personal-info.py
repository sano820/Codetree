n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.
answer = []
for i in range(5):
    answer.append((name[i],height[i], weight[i]))

def n():
    answer.sort(key = lambda x : x[0])
    print("name")
    for i in range(5):
        print(*answer[i])

def h():
    answer.sort(key = lambda x : -x[1])
    print("height")
    for i in range(5):
        print(*answer[i])

n()
print()
h()

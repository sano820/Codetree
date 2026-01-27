n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
def distance(point):
    x, y = point
    return abs(x) + abs(y)

new_points= []
for ind, point in points:
    new_points.append((ind, distance(point)))

new_points.sort(key = lambda x : x[1])
for i, _ in new_points:
    print(i+1)
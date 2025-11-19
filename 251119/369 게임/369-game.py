n = int(input())
count = 1
while count <= n:
    if count % 3 == 0 or count in [3,6,9]:
        print(0, end = ' ')
    else:
        print(count, end = ' ')
    count += 1
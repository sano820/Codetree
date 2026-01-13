n = int(input())

# Please write your code here.
def print_up(n):
    if n == 0:
        return
    print_up(n - 1)
    print(n, end=' ')

def print_down(n):
    if n == 0:
        return
    print(n, end=' ')
    print_down(n - 1)

print_up(n)
print()
print_down(n)




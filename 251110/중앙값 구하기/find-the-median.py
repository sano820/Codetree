A, B, C = map(int, input().split())

if A > B > C or A < B < C:
    print(B)
elif A < C < B or B<C<A:
    print(C)
else:
    print(A)
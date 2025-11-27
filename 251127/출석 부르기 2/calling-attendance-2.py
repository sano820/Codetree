A = {1 : "John", 2:"Tom", 3:"Paul", 4:"Sam"}

while True:
    n = int(input())
    if n in A.keys():
        print(A[n])
    else:
        print("Vacancy")
        break
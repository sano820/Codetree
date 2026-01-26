n = int(input())
name = []
korean = []
english = []
math = []

for _ in range(n):
    student_info = input().split()
    name.append(student_info[0])
    korean.append(int(student_info[1]))
    english.append(int(student_info[2]))
    math.append(int(student_info[3]))

# Please write your code here.
student = {}
for i in range(len(name)):
    student[name[i]] = (korean[i], english[i], math[i])


answer = sorted(student, key = lambda x : (student[x][0], student[x][1], student[x][2]), reverse = True)
for n in answer:
    print(n, student[n][0], student[n][1], student[n][2])

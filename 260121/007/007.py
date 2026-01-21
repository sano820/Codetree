secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Code:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

code = Code(secret_code, meeting_point, time)

print(f"secret code : {code.secret_code}")
print(f"meeting point : {code.meeting_point}")
print(f"time : {code.time}")

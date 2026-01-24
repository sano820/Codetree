unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class answer:
    def __init__(self, unlock_code, wire_color, seconds):
        self.code = f"code : {unlock_code}"
        self.color = f"color : {wire_color}"
        self.seconds = f"second : {seconds}"


answer = answer(unlock_code, wire_color, seconds)

print(answer.code)
print(answer.color)
print(answer.seconds)

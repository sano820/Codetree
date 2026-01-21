user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class answer:
    def __init__(self, user_id = "codetree", user_level = 10):
        self.id = f"user {user_id}"
        self.level = f"lv {user_level}"

sol1 = answer("codetree", 10)
sol2 = answer(user2_id, user2_level)


print(sol1.id, sol1.level)
print(sol2.id, sol2.level)
n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class sol:
    def __init__(self, name, street_address, region):
        self.name = name
        self.add = street_address
        self.reg = region
    
    def solution(self):
        answer = {}
        for i, n in enumerate(self.name):
            answer[n] = i

        # 정렬 결과를 변수로 받아야 함
        sorted_name = sorted(self.name)

        # 사전순으로 가장 느린 이름
        max_name = sorted_name[-1]
        ind = answer[max_name]

        print(f"name {max_name}")
        print(f"addr {self.add[ind]}")
        print(f"city {self.reg[ind]}")

answer = sol(name, street_address, region)
answer.solution()

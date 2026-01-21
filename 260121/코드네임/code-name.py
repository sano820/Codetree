MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.
class answer:
    def __init__(self, codenames, scores):
        self.info0 = (codenames[0], scores[0])
        self.info1 = (codenames[1], scores[1])
        self.info2 = (codenames[2], scores[2])
        self.info3 = (codenames[3], scores[3])
        self.info4 = (codenames[4], scores[4])    

sol = answer(codenames, scores)

solution = [sol.info0, sol.info1, sol.info2, sol.info3, sol.info4]
print(min(solution)[0], min(solution)[1])
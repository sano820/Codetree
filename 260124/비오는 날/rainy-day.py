n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class sol:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def answer(self):

        rain_dates = []
        for i, w in enumerate(self.weather):
            if w == "Rain":
                rain_dates.append(i)

        earliest = rain_dates[0]
        for i in rain_dates:
            if self.date[i] < self.date[earliest]:
                earliest = i

        print(f"{self.date[earliest]} {self.day[earliest]} {self.weather[earliest]}")

s = sol(date, day, weather)
s.answer()
            